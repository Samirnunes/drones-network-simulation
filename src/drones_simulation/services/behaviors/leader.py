import time

import numpy as np

from drones_simulation.config import TIMESTEP
from drones_simulation.log import logger

from ...models.behavior import BaseBehavior
from ...models.message import Heartbeat, Message, Move, Stop


class Leader(BaseBehavior):

    def run(self) -> None:
        i = 0
        while True:
            time.sleep(TIMESTEP)
            if (
                np.linalg.norm(self.drone.position - self.target) > 2
            ):  # TODO: parameterize distance to target to be considered as win
                self._move(self.target)
                i += 1
                if i % 2 == 0:
                    time.sleep(TIMESTEP / 9)
                    self._broadcast(Heartbeat(self.drone.position))
            else:
                self._stop()

    def _move(self, target: np.ndarray) -> None:
        super()._move(target)
        logger.info("Leader position: " + np.array2string(self.drone.position))
        self._broadcast(Move(self.target))

    def _broadcast(self, message: Message) -> None:
        self.connector.broadcast(message)

    def _stop(self) -> None:
        super()._stop()
        logger.info(
            "Leader reached target at position " + np.array2string(self.drone.position)
        )
        self._broadcast(Stop())
