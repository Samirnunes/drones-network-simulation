import sys
from logging import INFO, StreamHandler, getLogger

logger = getLogger("drones-simulation")
logger.addHandler(StreamHandler(sys.stdout))
logger.setLevel(INFO)
