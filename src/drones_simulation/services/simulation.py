from ..config import TCP_DRONE_SIMULATION_CONFIG, SimulationConfig
from ..log import logger
from ..models.base import BaseBehavior
from ..services.behaviors import BehaviorRouter
from ..services.connectors import TCPConnector


class TCPDroneSimulation:

    CONFIG: SimulationConfig = TCP_DRONE_SIMULATION_CONFIG

    def __init__(self) -> None:
        connector = TCPConnector()
        self._behavior: type[BaseBehavior] = BehaviorRouter.route(
            self.CONFIG.DRONE_BEHAVIOR
        )(connector)
        logger.info(
            f"Loaded behavior {self._behavior.__class__.__name__} with {connector.__class__.__name__}"
        )

    def run(self) -> None:
        # logger.info("Starting simulation...")
        # steps = self._behavior.steps()
        # while True:
        #    next(steps)
        pass
