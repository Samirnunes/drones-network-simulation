from abc import ABC, abstractmethod
from typing import Dict

from drones_simulation.models import Communicator, Drone


class Behavior(ABC):
    """
    Controls drone's behavior.
    There are two types of actions: local and distributed.
    Local actions doesn't need a communicator.
    Distributed ones need a communicator as a parameter to communicate with other drones.
    """

    def __init__(self, drone: Drone, communicator: Communicator) -> None:
        self._drone = drone
        self._communicator = communicator
        self._init_drone()

    @abstractmethod
    def _init_drone(self):
        raise NotImplementedError

    @abstractmethod
    def steps(self):
        """
        Must implement a generator for drone's behavior using `yield`.
        """
        raise NotImplementedError


class Attacker(Behavior):

    def _init_drone(self):
        self._drone.pos = 0
        self._drone.vel = 0

    def steps(self):
        pass


class BehaviorRouter:
    _BEHAVIOR_MAP: Dict[str, Behavior] = {"attacker": Attacker}

    @classmethod
    def route(cls, key: str) -> Behavior:
        return cls._BEHAVIOR_MAP[key]
