from dataclasses import dataclass

import numpy as np


@dataclass
class Drone:
    position: np.ndarray
    velocity: np.ndarray
    radius: float
    signal_weakness: float | None
    isAlive: bool
