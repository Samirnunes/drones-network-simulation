import numpy as np

from ...models.behavior import BaseBehavior
from ...models.message import Message, Move


class Leader(BaseBehavior):

    def run(self) -> None:
        while True:
            self._move_to_package_pos()

    def _move_to_package_pos(self) -> None:
        direction = self.package_pos - self.drone.position
        direction = direction / np.linalg.norm(direction)

        new_velocity = self.drone.velocity + 0.2 * direction
        self.drone.velocity = (
            np.linalg.norm(self.drone.velocity)
            * new_velocity
            / np.linalg.norm(new_velocity)
        )

        self.drone.position += self.drone.position + self.drone.velocity
        self._broadcast(Move(direction))

    def _broadcast(self, message: Message) -> None:
        self.connector.broadcast(message)
