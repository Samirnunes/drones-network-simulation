from typing import List

from pydantic_settings import BaseSettings


class MainConfig(BaseSettings):
    BEHAVIOR: str = "on_mission"


class SimulationConfig(BaseSettings):
    PACKAGE_POS: List = [10, 20, 30]


class ConnectorConfig(BaseSettings):
    TYPE: str = "tcp"
    HOST: str = "0.0.0.0"
    PORT: int = "80"


MAIN_CONFIG = MainConfig()
SIMULATION_CONFIG = SimulationConfig()
CONNECTOR_CONFIG = ConnectorConfig()
