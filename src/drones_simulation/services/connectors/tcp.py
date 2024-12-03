import socket

from drones_simulation.config import CONNECTOR_CONFIG, ConnectorConfig
from drones_simulation.models.base import BaseConnector


class TCPConnector(BaseConnector):

    CONFIG: ConnectorConfig = CONNECTOR_CONFIG
