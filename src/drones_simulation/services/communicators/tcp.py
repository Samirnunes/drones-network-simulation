import socket

from drones_simulation.config import TCP_COMMUNICATOR_CONFIG, CommunicatorConfig


class TCPCommunicator:

    CONFIG: CommunicatorConfig = TCP_COMMUNICATOR_CONFIG
