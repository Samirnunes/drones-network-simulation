import pickle
import socket
import threading
from typing import Any, List

from drones_simulation.log import logger

from ...models.connector import BaseConnector
from ...models.message import Message


class TCPConnector(BaseConnector):

    def start_server(self) -> None:
        """Start the server to listen for incoming messages."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", 80))
        self.server_socket.listen(5)
        self.running = True
        logger.info(f"Server started on port 80")

        self.hosts = [f"drone-{i}" for i in range(1, self._config.DRONES_NUMBER + 1)]
        self.client_sockets: List[Any] = []
        threading.Thread(target=self._accept_clients, daemon=True).start()

        self.received_message: Message | None = None

    def _accept_clients(self) -> None:
        """Accept incoming client connections."""
        while self.running:
            client_socket, address = self.server_socket.accept()
            logger.info(f"Client connected from {address}")
            threading.Thread(
                target=self._handle_client, args=(client_socket,), daemon=True
            ).start()

    def _handle_client(self, client_socket: Any) -> None:
        """Handle communication with a connected client."""
        while self.running:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = pickle.loads(data)
                self.received_message = message
            except (ConnectionResetError, BrokenPipeError, EOFError) as e:
                logger.error(f"Error while receiving message: {e}")
                break
        client_socket.close()

    def connect_to_hosts(self) -> None:
        """Establish connections to the predefined list of hosts."""
        while len(self.client_sockets) < len(self.hosts):
            for host in self.hosts:
                if any(
                    socket.getpeername()[0] == host for socket in self.client_sockets
                ):
                    continue

                try:
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((host, 80))
                    self.client_sockets.append(client_socket)
                    logger.info(f"Connected to {host}:80")
                except socket.error as e:
                    logger.error(f"Failed to connect to {host}:80 - {e}")

    def broadcast(self, message: Message) -> None:
        """Send a message to all connected hosts."""
        serialized_message = pickle.dumps(message)
        for client_socket in self.client_sockets:
            try:
                client_socket.sendall(serialized_message)
                logger.info(f"Sent message: {message}")
            except (ConnectionResetError, BrokenPipeError, EOFError) as e:
                logger.error(f"Failed to send message to a client - {e}")

    def stop(self) -> None:
        """Stop the server and close all connections."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        for client_socket in self.client_sockets:
            client_socket.close()
        logger.info("Server stopped and all connections closed")
