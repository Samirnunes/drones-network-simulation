import time
from io import BytesIO
from typing import Dict, List

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from drones_simulation.config import TIMESTEP, ConnectorConfig
from drones_simulation.log import logger
from drones_simulation.models.message import InformObserver
from drones_simulation.services.connectors.router import ConnectorRouter


class Observer:
    def __init__(
        self,
        connector_config: ConnectorConfig,
    ) -> None:
        self.connector = ConnectorRouter.route(connector_config.TYPE)(connector_config)
        self.connector.start_server()
        self.connector.connect_to_hosts()

        self.fig, self.ax = plt.subplots()
        self.scat = self.ax.scatter([], [])
        self.labels: Dict = {}

        self.ax.set_xlim(-2, 22)
        self.ax.set_ylim(-2, 22)

        self.ax.plot(10, 20, "rx", markersize=10, label="Target")
        self.ax.legend()

        plt.ion()
        plt.show()

    def run(self) -> None:
        while True:
            self._receive_message()
            time.sleep(TIMESTEP / 10)

    def _receive_message(self) -> None:
        if len(self.connector.received_messages) > 0:
            for message in self.connector.received_messages:
                if isinstance(message, InformObserver):
                    logger.info("Observed a new pattern: rendering image...")
                    self._update_plot(message)
            self.connector.received_messages.clear()

    def _update_plot(self, message: InformObserver) -> None:
        name = message.name
        position = message.position
        current_positions: List = list(self.scat.get_offsets())

        if name in self.labels:
            index = self.labels[name]
            current_positions[index] = position
            self.scat.set_offsets(current_positions)
        else:
            self.scat.set_offsets(current_positions + [position])
            index = len(current_positions)
            self.labels[name] = index

    def render(self) -> bytes:
        canvas = FigureCanvas(self.fig)
        buf = BytesIO()
        canvas.print_png(buf)
        buf.seek(0)
        return buf.getvalue()
