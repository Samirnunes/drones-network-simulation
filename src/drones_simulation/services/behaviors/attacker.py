import time

import numpy as np

from drones_simulation.config.config import TIMESTEP, BehaviorConfig, ConnectorConfig
from drones_simulation.models.message import Message, Move

from ...models.behavior import BaseBehavior


class Attacker(BaseBehavior):

    def __init__(
        self,
        behavior_config: BehaviorConfig,
        connector_config: ConnectorConfig,
    ) -> None:
        super().__init__(behavior_config, connector_config)
        self.drones_number = connector_config.DRONES_NUMBER
        self.rand = np.random.RandomState(0)
        self.fake_targets = list(self.rand.uniform(0, 20, 2 * (self.drones_number - 1)))

    def run(self) -> None:
        time.sleep(30 * TIMESTEP)

        while True:
            for i in range(0, self.drones_number - 1):
                self.connector.send_to_drone(
                    Move(
                        np.array(
                            [self.fake_targets[i]]
                            + [self.fake_targets[i + self.drones_number - 1]]
                        )
                    ),
                    i + 1,
                )
            time.sleep(2 * TIMESTEP)

    def _broadcast(self, message: Message) -> None:
        self.connector.broadcast(message)
