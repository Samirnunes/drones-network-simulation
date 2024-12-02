from typing import Dict

from ...models.base import BaseBehavior
from ...services.behaviors import Invaded
from ...services.behaviors.on_mission import OnMission


class BehaviorRouter:

    _BEHAVIOR_MAP: Dict[str, type[BaseBehavior]] = {
        "invaded": Invaded,
        "on-mission": OnMission,
    }

    @classmethod
    def route(cls, key: str) -> type[BaseBehavior]:
        return cls._BEHAVIOR_MAP[key]
