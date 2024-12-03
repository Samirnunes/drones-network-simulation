from typing import Dict

from ...models.base import BaseBehavior
from ...services.behaviors import InvadedLeader, Leader, OnMission


class BehaviorRouter:

    _BEHAVIOR_MAP: Dict[str, type[BaseBehavior]] = {
        "leader": Leader,
        "invaded-leader": InvadedLeader,
        "on-mission": OnMission,
    }

    @classmethod
    def route(cls, key: str) -> type[BaseBehavior]:
        return cls._BEHAVIOR_MAP[key.lower()]
