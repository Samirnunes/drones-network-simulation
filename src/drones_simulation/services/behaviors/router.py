from typing import Dict

from drones_simulation.models.base import BaseBehavior
from drones_simulation.services.behaviors import Attacker


class BehaviorRouter:

    _BEHAVIOR_MAP: Dict[str, BaseBehavior] = {"attacker": Attacker}

    @classmethod
    def route(cls, key: str) -> BaseBehavior:
        return cls._BEHAVIOR_MAP[key]
