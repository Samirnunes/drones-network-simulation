from ..config import BEHAVIOR_CONFIG, CONNECTOR_CONFIG, DRONE_CONFIG
from .simulation import Simulation


class Main:

    def __init__(self) -> None:
        self._simulation = Simulation(DRONE_CONFIG, BEHAVIOR_CONFIG, CONNECTOR_CONFIG)

    def run(self) -> None:
        self._simulation.run()
