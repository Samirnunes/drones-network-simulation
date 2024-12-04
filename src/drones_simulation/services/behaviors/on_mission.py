import numpy as np

from drones_simulation.log import logger

from ...models.behavior import BaseBehavior
from ...models.message import Message, Move, Stop


class OnMission(BaseBehavior):
    """
    Drone oriented by a leader. The objective is to reach the target's location.
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
            if isinstance(message, Stop):
                self._stop()

    def _move(self, target: np.ndarray) -> None:
        super()._move(target)
        logger.info("Drone position: " + np.array2string(self.drone.position))

    def _stop(self) -> None:
        super()._stop()
        logger.info(
            "Drone stopped at position: " + np.array2string(self.drone.position)
        )
