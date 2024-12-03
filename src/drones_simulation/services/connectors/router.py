from typing import Dict

from ...models.base import BaseConnector
from .tcp import TCPConnector


class ConnectorRouter:

    _CONNECTOR_MAP: Dict[str, type[BaseConnector]] = {
        "tcp": TCPConnector,
    }

    @classmethod
    def route(cls, key: str) -> type[BaseConnector]:
        return cls._CONNECTOR_MAP[key.lower()]
