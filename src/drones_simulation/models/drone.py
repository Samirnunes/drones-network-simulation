from dataclasses import dataclass

import numpy as np


@dataclass
class Drone:
    pos: np.ndarray
    vel: np.ndarray
