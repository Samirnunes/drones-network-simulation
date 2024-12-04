import pickle
import socket
import threading
import time
from typing import Any, Dict, List

from drones_simulation.log import logger

from ...models.connector import BaseConnector
from ...models.message import Message


class TCPConnector(BaseConnector):

    def start_server(self) -> None:
        """Start the server to listen for incoming messages."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self._config.HOST, self._config.PORT))
        self.server_socket.listen(5)
        self.running = True
        logger.info(f"Server started on port {self._config.PORT}")

        self.hosts = [f"drone-{i}" for i in range(1, self._config.DRONES_NUMBER + 1)]
        self.hosts = self.hosts + ["observer"]
        self.hosts.remove(self._config.NAME)

        self.client_sockets: Dict[str, Any] = dict.fromkeys(self.hosts, None)
        threading.Thread(target=self._accept_clients, daemon=True).start()

        self.received_messages: List[Message] = []

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
                data = client_socket.recv(2048)
                if not data:
                    break
                self.received_messages.append(pickle.loads(data))
            except Exception as e:
                logger.error(f"Error while receiving message: {e}")
                time.sleep(5)
                break
        client_socket.close()

    def connect_to_hosts(self) -> None:
        """Establish connections to the predefined list of hosts."""
        while any([value is None for value in self.client_sockets.values()]):
            for host in self.hosts:
                if self.client_sockets[host] is not None:
                    continue
                try:
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((host, self._config.PORT))
                    self.client_sockets[host] = client_socket
                    logger.info(f"Connected to {host}:{self._config.PORT}")
                except socket.error as e:
                    logger.error(
                        f"Failed to connect to {host}:{self._config.PORT} - {e}"
                    )
                    time.sleep(10)

    def broadcast(self, message: Message) -> None:
        """Send a message to all connected hosts, except the observer."""
        serialized_message = pickle.dumps(message)
        for client_socket in self.client_sockets.values():
            try:
                client_socket.sendall(serialized_message)
                logger.info(f"Sent message: {message}")
                time.sleep(2)
            except Exception as e:
                logger.error(f"Failed to send message to a client - {e}")
                time.sleep(2.5)

    def send_to_observer(self, message: Message) -> None:
        """Send a message to a specific client."""
        serialized_message = pickle.dumps(message)
        try:
            self.client_sockets["observer"].sendall(serialized_message)
            logger.info(f"Sent message: {message}")
            time.sleep(2)
        except Exception as e:
            logger.error(f"Failed to send message to the client - {e}")
            time.sleep(4)

    def stop(self) -> None:
        """Stop the server and close all connections."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        for client_socket in self.client_sockets.values():
            client_socket.close()
        logger.info("Server stopped and all connections closed")
