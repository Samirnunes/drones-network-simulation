from abc import ABC, abstractmethod

import numpy as np

from ..config import ConnectorConfig
from .message import Message


class BaseConnector(ABC):
    def __init__(self, config: ConnectorConfig) -> None:
        self._config = config
        self.received_message: Message | None = None

    @abstractmethod
    def start_server(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def broadcast(self, message: Message) -> None:
        raise NotImplementedError

    @abstractmethod
    def connect_to_hosts(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError
