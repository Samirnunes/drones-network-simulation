from abc import ABC, abstractmethod

import numpy as np

from drones_simulation.log import logger

from ..config import BehaviorConfig, ConnectorConfig
from ..models.message import InformObserver
from ..services.connectors.router import ConnectorRouter
from .drone import Drone


class BaseBehavior(ABC):
    """
    Controls drone's behavior.
    There are two types of actions: local and distributed.
    Local actions doesn't need a connector.
    Distributed ones need a connector as a parameter to communicate with other drones.
    """

    def __init__(
        self,
        behavior_config: BehaviorConfig,
        connector_config: ConnectorConfig,
    ) -> None:
        self.drone = Drone(
            np.array([behavior_config.INITIAL_POS_X, behavior_config.INITIAL_POS_Y]),
            np.array([behavior_config.INITIAL_VEL_X, behavior_config.INITIAL_VEL_Y]),
            behavior_config.RADIUS,
            None,
            True,
        )
        self.name = connector_config.NAME
        self.connector = ConnectorRouter.route(connector_config.TYPE)(connector_config)
        self.connector.start_server()
        self.connector.connect_to_hosts()

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def _move(self, leader_position: np.ndarray) -> None:
        direction = leader_position - self.drone.position
        direction = direction / np.linalg.norm(direction)
        if self.drone.signal_weakness is None:
            new_velocity = self.drone.velocity + direction
        else:
            new_velocity = self.drone.velocity + self.drone.signal_weakness * direction
        self.drone.velocity = (
            np.linalg.norm(self.drone.velocity)
            * new_velocity
            / np.linalg.norm(new_velocity)
        )

        self.drone.position += self.drone.velocity
        self._inform_observer()

    def _stop(self) -> None:
        self.drone.velocity = np.array([0, 0])

    def _inform_observer(self) -> None:
        self.connector.send_to_observer(InformObserver(self.name, self.drone.position))
