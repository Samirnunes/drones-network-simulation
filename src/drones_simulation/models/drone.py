from drones_simulation.config import DRONE_CONFIG
from drones_simulation.log import logger
from drones_simulation.models import Behavior, BehaviorRouter, Communicator


class Drone:

    CONFIG = DRONE_CONFIG

    def __init__(self) -> None:
        self._behavior: Behavior = BehaviorRouter.route(self.CONFIG.env.BEHAVIOR)(
            self, Communicator()
        )
        logger.info(f"Loaded behavior: {self._behavior.__class__.__name__}")

    def run(self) -> None:
        steps = self._behavior.steps()
        while True:
            next(steps)
