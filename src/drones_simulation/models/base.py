from abc import ABC, abstractmethod

from drones_simulation.config import ConnectorConfig
from drones_simulation.models import Drone


class BaseConnector(ABC):
    CONFIG: ConnectorConfig


class BaseBehavior(ABC):
    """
    Controls drone's behavior.
    There are two types of actions: local and distributed.
    Local actions doesn't need a connector.
    Distributed ones need a connector as a parameter to communicate with other drones.
    """

    def __init__(self, connector: BaseConnector) -> None:
        self._connector = connector
        self._drone: Drone
        self._init_drone()

    @abstractmethod
    def _init_drone(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def steps(self) -> None:
        """
        Must implement a generator for drone's behavior using `yield`.
        """
        raise NotImplementedError
