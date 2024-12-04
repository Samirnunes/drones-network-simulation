import time

import numpy as np

from drones_simulation.log import logger

from ...models.behavior import BaseBehavior
from ...models.message import Message, Move, Stop


class Leader(BaseBehavior):

    def run(self) -> None:
        while True:
            time.sleep(1)
            if np.linalg.norm(self.drone.position - self.target) > 2:
                self._move(self.target)
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
