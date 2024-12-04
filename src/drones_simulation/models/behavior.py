from abc import ABC, abstractmethod

import numpy as np

from ..config import BehaviorConfig, ConnectorConfig
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
            True,
        )
        self.target = np.array(behavior_config.TARGET)
        self.connector = ConnectorRouter.route(connector_config.TYPE)(connector_config)
        self.connector.start_server()
        self.connector.connect_to_hosts()

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def _move(self, target: np.ndarray) -> None:
        direction = target - self.drone.position
        direction = direction / np.linalg.norm(direction)

        new_velocity = self.drone.velocity + 0.8 * direction
        self.drone.velocity = (
            np.linalg.norm(self.drone.velocity)
            * new_velocity
            / np.linalg.norm(new_velocity)
        )

        self.drone.position += self.drone.velocity

    def _stop(self) -> None:
        self.drone.velocity = np.array([0, 0])
