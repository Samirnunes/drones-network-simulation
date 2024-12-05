from typing import Dict

from ...models.behavior import BaseBehavior
from . import Attacker, Leader, OnMission


class BehaviorRouter:

    _BEHAVIOR_MAP: Dict[str, type[BaseBehavior]] = {
        "leader": Leader,
        "attacker": Attacker,
        "on-mission": OnMission,
    }

    @classmethod
    def route(cls, key: str) -> type[BaseBehavior]:
        return cls._BEHAVIOR_MAP[key.lower()]
