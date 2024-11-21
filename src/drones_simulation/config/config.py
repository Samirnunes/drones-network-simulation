from typing import List
from pydantic_settings import BaseSettings


class _DRONE_ENVS(BaseSettings):
    BEHAVIOR: str
    INITIAL_POS: List[float]
    INITIAL_VEL: List[float]


class _COMMUNICATOR_ENVS(BaseSettings):
    HOST: str
    PORT: int


class _DroneConfig(BaseSettings):
    env: _DRONE_ENVS = _DRONE_ENVS()


class _CommunicatorConfig(BaseSettings):
    env: _COMMUNICATOR_ENVS = _COMMUNICATOR_ENVS()


DRONE_CONFIG = _DroneConfig()
COMMUNICATOR_CONFIG = _CommunicatorConfig()
