from ..config import CONNECTOR_CONFIG, MAIN_CONFIG, SIMULATION_CONFIG
from .simulations.router import SimulationRouter


class Main:

    def __init__(self) -> None:
        self._simulation = SimulationRouter.route(MAIN_CONFIG.BEHAVIOR)(
            MAIN_CONFIG.BEHAVIOR, SIMULATION_CONFIG, CONNECTOR_CONFIG
        )

    def run(self) -> None:
        self._simulation.run()
