import ast
from typing import List

import numpy as np
from pydantic import field_validator
from pydantic_settings import BaseSettings


class DroneConfig(BaseSettings):
    BEHAVIOR: str = "on-mission"


class BehaviorConfig(BaseSettings):
    PACKAGE_POS: List = [10, 20]
    INITIAL_POS_X: float = 0
    INITIAL_POS_Y: float = 0
    INITIAL_VEL: List = [1, 1]


class ConnectorConfig(BaseSettings):
    TYPE: str = "tcp"
    HOST: str = "0.0.0.0"
    PORT: int = "80"
    DRONES_NUMBER: int = 4


DRONE_CONFIG = DroneConfig()
BEHAVIOR_CONFIG = BehaviorConfig()
CONNECTOR_CONFIG = ConnectorConfig()
