from drones_simulation.config import ConnectorConfig
from drones_simulation.models.behavior import BaseBehavior

from ..config import BehaviorConfig, DroneConfig
from ..log import logger
from ..services.behaviors.router import BehaviorRouter


class Simulation:

    def __init__(
        self,
        drone_config: DroneConfig,
        behavior_config: BehaviorConfig,
        connector_config: ConnectorConfig,
    ) -> None:
        self._behavior: BaseBehavior = BehaviorRouter.route(drone_config.BEHAVIOR)(
            behavior_config, connector_config
        )

        logger.info(
            f"Loaded behavior {self._behavior.__class__.__name__} with {connector_config.__class__.__name__}"
        )

    def run(self) -> None:
        logger.info("Starting simulation...")
        self._behavior.run()
