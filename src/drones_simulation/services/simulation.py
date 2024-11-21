from drones_simulation.config import TCP_DRONE_SIMULATION_CONFIG, SimulationConfig
from drones_simulation.log import logger
from drones_simulation.models.base import BaseBehavior
from drones_simulation.services.behaviors import BehaviorRouter
from drones_simulation.services.connectors import TCPConnector


class TCPDroneSimulation:

    CONFIG: SimulationConfig = TCP_DRONE_SIMULATION_CONFIG

    def __init__(self) -> None:
        connector = TCPConnector()
        self._behavior: BaseBehavior = BehaviorRouter.route(self.CONFIG.DRONE_BEHAVIOR)(
            connector
        )
        logger.info(
            f"Loaded behavior {self._behavior.__class__.__name__} with {connector.__class__.__name__}"
        )

    def run(self) -> None:
        logger.info("Starting simulation...")
        steps = self._behavior.steps()
        while True:
            next(steps)
