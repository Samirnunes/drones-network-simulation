import numpy as np

from drones_simulation.models import Drone
from drones_simulation.models.base import BaseBehavior


class OnMission(BaseBehavior):

    def _init_drone(self):
        self._drone = Drone(np.array([0, 0, 0]), np.array([1, 1, 1]))

    def steps(self):
        pass
