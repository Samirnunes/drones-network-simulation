from typing import List

import numpy as np

from drones_simulation.config import DRONE_INITIAL_CONFIG
from drones_simulation.log import logger
from drones_simulation.models import Behavior, BehaviorRouter, Communicator


class Drone:

    def __init__(self) -> None:
        self.pos: np.ndarray
        self.vel: np.ndarray

        self._behavior: Behavior = BehaviorRouter.route(DRONE_INITIAL_CONFIG.BEHAVIOR)(
            self, Communicator()
        )
        logger.info(f"Loaded behavior: {self._behavior.__class__.__name__}")

    def run(self) -> None:
        steps = self._behavior.steps()
        while True:
            next(steps)
