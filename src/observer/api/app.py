from contextlib import asynccontextmanager
from threading import Thread
from typing import AsyncGenerator

from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

from drones_simulation.config import CONNECTOR_CONFIG
from observer import Observer

observer = Observer(CONNECTOR_CONFIG)


def start_observer() -> None:
    observer.run()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    observer_thread = Thread(target=start_observer, daemon=True)
    observer_thread.start()
    yield


app = FastAPI(title="observer", lifespan=lifespan)


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    """Serve the HTML page with the Matplotlib image."""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Drones Simulation</title>
    </head>
    <body>
        <h1>Drones Simulation</h1>
        <img src="/plot" alt="Simulation Plot" style="border: 1px solid black;" />
        <p>Refresh to see updates.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/plot")
async def get_plot() -> Response:
    """Serve the current plot image."""
    image = observer.render()
    return Response(content=image, media_type="image/png")
