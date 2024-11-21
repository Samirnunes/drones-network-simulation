from typing import List

from pydantic_settings import BaseSettings


class _DroneConfig(BaseSettings):
    BEHAVIOR: str


class _CommunicatorConfig(BaseSettings):
    HOST: str
    PORT: int


DRONE_INITIAL_CONFIG = _DroneConfig()
COMMUNICATOR_CONFIG = _CommunicatorConfig()
