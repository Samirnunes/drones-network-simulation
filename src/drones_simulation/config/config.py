from pydantic_settings import BaseSettings


class SimulationConfig(BaseSettings):
    DRONE_BEHAVIOR: str = "attacker"


class ConnectorConfig(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = "80"


TCP_DRONE_SIMULATION_CONFIG = SimulationConfig()
TCP_CONNECTOR_CONFIG = ConnectorConfig()
