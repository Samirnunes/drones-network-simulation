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
            np.array([1, 1]),
        )
        self.package_pos = np.array(behavior_config.PACKAGE_POS)
        self.connector = ConnectorRouter.route(connector_config.TYPE)(connector_config)
        self.connector.start_server()
        self.connector.connect_to_hosts()

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError
