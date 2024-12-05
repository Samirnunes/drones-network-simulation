import numpy as np

from drones_simulation.log import logger

from ...models.behavior import BaseBehavior
from ...models.message import Heartbeat, Move, Stop


class OnMission(BaseBehavior):
    """
    Drone oriented by a leader. The objective is to reach the target's location.
    """

    def run(self) -> None:
        while self.drone.isAlive:
            self._receive_message()

    def _receive_message(self) -> None:
        if len(self.connector.received_messages) > 0:
            for message in self.connector.received_messages:
                if isinstance(message, Move):
                    self._move(message.target)
                if isinstance(message, Stop):
                    self._stop()
                if isinstance(message, Heartbeat):
                    self._evaluateHeartbeat(message.position)
            self.connector.received_messages.clear()

    def _move(self, target: np.ndarray) -> None:
        super()._move(target)
        logger.info("Drone position: " + np.array2string(self.drone.position))

    def _stop(self) -> None:
        super()._stop()
        self.drone.isAlive = False
        logger.info(
            "Drone stopped at position: " + np.array2string(self.drone.position)
        )

    def _evaluateHeartbeat(self, leader_position: np.ndarray) -> None:
        distance = np.linalg.norm(leader_position - self.drone.position)
        self.drone.signal_weakness = 3 * distance
        if distance > self.drone.radius:
            self.drone.isAlive = False
            logger.info("Drone too far away, terminating.")
