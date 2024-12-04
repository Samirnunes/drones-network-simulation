from typing import List

from pydantic_settings import BaseSettings


class DroneConfig(BaseSettings):
    BEHAVIOR: str = "on-mission"


class BehaviorConfig(BaseSettings):
    PACKAGE_POS: List = [10, 20]
    INITIAL_POS: List = [0, 0]
    INITIAL_VEL: List = [1, 1]


class ConnectorConfig(BaseSettings):
    TYPE: str = "tcp"
    HOST: str = "0.0.0.0"
    PORT: int = "80"
    DRONES_NUMBER: int = 4


DRONE_CONFIG = DroneConfig()
BEHAVIOR_CONFIG = BehaviorConfig()
CONNECTOR_CONFIG = ConnectorConfig()
