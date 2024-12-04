import time

import numpy as np

from drones_simulation.log import logger

from ...config import BehaviorConfig, ConnectorConfig
from ...models.behavior import BaseBehavior
from ...models.message import Heartbeat, Message, Move, Stop


class Leader(BaseBehavior):

    def __init__(
        self,
        behavior_config: BehaviorConfig,
        connector_config: ConnectorConfig,
    ) -> None:
        super().__init__(behavior_config, connector_config)
        self.target = np.array(behavior_config.TARGET)

    def run(self) -> None:
        i = 0
        while True:
            time.sleep(1)
            if (
                np.linalg.norm(self.drone.position - self.target) > 2
            ):  # TODO: parameterize distance to target to be considered as win
                self._move(self.target)
                i += 1
                if i % 2 == 0:
                    time.sleep(0.1)
                    self._broadcast(Heartbeat(self.drone.position))
            else:
                self._stop()

    def _move(self, target: np.ndarray) -> None:
        super()._move(target)
        logger.info("Leader position: " + np.array2string(self.drone.position))
        self._broadcast(Move(self.target))

    def _broadcast(self, message: Message) -> None:
        self.connector.broadcast(message)

    def _stop(self) -> None:
        super()._stop()
        logger.info(
            "Leader reached target at position " + np.array2string(self.drone.position)
        )
        self._broadcast(Stop())
