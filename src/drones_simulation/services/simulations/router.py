from typing import Dict

from ...models.base import BaseSimulation
from .invaded import InvadedSimulation
from .on_mission import OnMissionSimulation


class SimulationRouter:

    _SIMULATION_MAP: Dict[str, type[BaseSimulation]] = {
        "invaded": InvadedSimulation,
        "on-mission": OnMissionSimulation,
    }

    @classmethod
    def route(cls, key: str) -> type[BaseSimulation]:
        return cls._SIMULATION_MAP[key.lower()]
