import numpy as np

from drones_simulation.log import logger

from ...models.behavior import BaseBehavior
from ...models.message import Message, Move, Stop


class OnMission(BaseBehavior):
    """
    Drone oriented by a leader doing a package rescue mission. The objective is to reach the package's location.
    """

    def run(self) -> None:
        while True:
            self._receive_message()

    def _receive_message(self) -> None:
        if self.connector.received_message is not None:
            message = self.connector.received_message
            self.connector.received_message = None
            if isinstance(message, Move):
                self._move(message.target)

    def _move(self, target: np.ndarray) -> None:
        direction = target - self.drone.position
        direction = direction / np.linalg.norm(direction)

        new_velocity = self.drone.velocity + 0.8 * direction
        self.drone.velocity = (
            np.linalg.norm(self.drone.velocity)
            * new_velocity
            / np.linalg.norm(new_velocity)
        )

        logger.info("Drone position: " + np.array2string(self.drone.position))
        self.drone.position += self.drone.velocity
