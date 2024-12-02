import numpy as np

from ...models import Drone
from ...models.base import BaseBehavior


class Invaded(BaseBehavior):

    def _init_drone(self) -> None:
        self._drone = Drone(np.array([0, 0, 0]), np.array([1, 1, 1]))

    def steps(self) -> None:
        pass
