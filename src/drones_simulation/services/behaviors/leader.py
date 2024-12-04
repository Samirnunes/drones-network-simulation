import time

import numpy as np

from drones_simulation.log import logger

from ...models.behavior import BaseBehavior
from ...models.message import Message, Move


class Leader(BaseBehavior):

    def run(self) -> None:
        while True:
            time.sleep(1)
            self._move()

    def _move(self) -> None:
        direction = self.target - self.drone.position
        direction = direction / np.linalg.norm(direction)

        new_velocity = self.drone.velocity + 0.8 * direction
        self.drone.velocity = (
            np.linalg.norm(self.drone.velocity)
            * new_velocity
            / np.linalg.norm(new_velocity)
        )

        logger.info("Leader position: " + np.array2string(self.drone.position))
        self.drone.position += self.drone.velocity
        self._broadcast(Move(self.target))

    def _broadcast(self, message: Message) -> None:
        self.connector.broadcast(message)
