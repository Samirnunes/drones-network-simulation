from typing import List

from pydantic_settings import BaseSettings


class DroneConfig(BaseSettings):
    BEHAVIOR: str = "on-mission"


class BehaviorConfig(BaseSettings):
    TARGET: List = [10, 20]
    INITIAL_POS_X: float = 0
    INITIAL_POS_Y: float = 0
    INITIAL_VEL_X: float = 0.2
    INITIAL_VEL_Y: float = 0.2
    RADIUS: float = 3


class ConnectorConfig(BaseSettings):
    NAME: str = "drone-1"
    TYPE: str = "tcp"
    HOST: str = "0.0.0.0"
    PORT: int = 80
    DRONES_NUMBER: int = 3


TIMESTEP = 0.1

DRONE_CONFIG = DroneConfig()
BEHAVIOR_CONFIG = BehaviorConfig()
CONNECTOR_CONFIG = ConnectorConfig()
