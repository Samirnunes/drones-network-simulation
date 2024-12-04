from abc import ABC
from dataclasses import dataclass

import numpy as np


class Message(ABC):
    pass


@dataclass
class Move(Message):
    target: np.ndarray


@dataclass
class Stop(Message):
    pass


@dataclass
class Heartbeat(Message):
    position: np.ndarray


@dataclass
class InformObserver(Message):
    name: str
    position: np.ndarray
