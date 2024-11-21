from typing import Dict

from drones_simulation.models.base import BaseBehavior
from drones_simulation.services.behaviors import Attacker
from drones_simulation.services.behaviors.on_mission import OnMission


class BehaviorRouter:

    _BEHAVIOR_MAP: Dict[str, BaseBehavior] = {
        "attacker": Attacker,
        "on-mission": OnMission,
    }

    @classmethod
    def route(cls, key: str) -> BaseBehavior:
        return cls._BEHAVIOR_MAP[key]
