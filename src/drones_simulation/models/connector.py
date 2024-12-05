from abc import ABC, abstractmethod
from typing import List

from ..config import ConnectorConfig
from .message import Message


class BaseConnector(ABC):
    def __init__(self, config: ConnectorConfig) -> None:
        self._config = config
        self.received_messages: List[Message]

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

    @abstractmethod
    def send_to_drone(self, message: Message, index: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def send_to_observer(self, message: Message) -> None:
        raise NotImplementedError
