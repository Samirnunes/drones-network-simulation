from abc import ABC, abstractmethod

from drones_simulation.config import ConnectorConfig
from drones_simulation.models import Drone


class BaseConnector(ABC):
    CONFIG: ConnectorConfig


class BaseBehavior(ABC):
    """
    Controls drone's behavior.
    There are two types of actions: local and distributed.
    Local actions doesn't need a communicator.
    Distributed ones need a communicator as a parameter to communicate with other drones.
    """

    def __init__(self, communicator: BaseConnector) -> None:
        self._communicator = communicator
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
