from abc import ABC, abstractmethod
from typing import Self

import numpy as np

from drones_simulation.config import ConnectorConfig
from drones_simulation.models import Drone

from ..config import SimulationConfig
from ..log import logger
from ..services.behaviors.router import BehaviorRouter
from ..services.connectors.router import ConnectorRouter


class BaseConnector(ABC):
    CONFIG: ConnectorConfig


class BaseBehavior(ABC):
    """
    Controls drone's behavior.
    There are two types of actions: local and distributed.
    Local actions doesn't need a connector.
    Distributed ones need a connector as a parameter to communicate with other drones.
    """

    def __init__(
        self,
        connector_config: ConnectorConfig,
        package_pos: np.ndarray,
    ) -> None:
        self.connector = ConnectorRouter.route(connector_config.TYPE)(connector_config)
        self.package_pos = package_pos
        self.drone = Drone(np.array([0, 0, 0]), np.array([1, 1, 1]))

    @abstractmethod
    def steps(self) -> None:
        """
        Must implement a generator for drone's behavior using `yield`.
        """
        raise NotImplementedError


class BaseSimulation(ABC):
    def __init__(
        self,
        behavior: str,
        simulation_config: SimulationConfig,
        connector_config: ConnectorConfig,
    ) -> None:
        self._config = simulation_config
        self._connector = connector_config

        self._behavior: BaseBehavior = BehaviorRouter.route(behavior)(
            connector_config, self._config.PACKAGE_POS
        )

        logger.info(
            f"Loaded behavior {self._behavior.__class__.__name__} with {connector_config.__class__.__name__}"
        )

    def change_behavior(self, new_behavior: BaseBehavior) -> Self:
        drone = self._behavior.drone
        package_pos = self._behavior.package_pos
        self._behavior = new_behavior
        self._behavior.drone = drone
        self._behavior.package_pos = package_pos
        return self

    def change_package_pos(self, new_package_pos: np.ndarray) -> Self:
        self._behavior.package_pos = new_package_pos
        return self

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError
