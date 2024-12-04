import numpy as np

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
                self._move(message.direction)

    def _move(self, direction: np.ndarray) -> None:
        pass
