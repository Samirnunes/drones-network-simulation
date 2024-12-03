from abc import ABC
from dataclasses import dataclass

import numpy as np


class Message(ABC):
    pass


@dataclass
class Move(Message):
    direction: np.ndarray


@dataclass
class Stop(Message):
    pass
