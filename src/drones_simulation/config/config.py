from pydantic_settings import BaseSettings


class _DRONE_ENVS(BaseSettings):
    HOST: str
    PORT: int


class _DroneConfig(BaseSettings):
    env: _DRONE_ENVS = _DRONE_ENVS()


DRONE_CONFIG = _DroneConfig()
