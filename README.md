# Drones Simulation

## Content

A fleet of drones is flying towards a objective. There is a leader drone who regularly broadcasts the objective's position to the others. We simulate an attack where the leader drone is compromised and now sends to each drone a fake objective position. To maintain strong connectivity, each drone must remain within a certain radius of at least one other drone. If a drone becomes too isolated and exceeds this radius, it loses its connection and self-terminates.

`TODO`:

- complete `Invaded` and `OnMission` behaviors in `src/drones_simulation/services/behaviors`.

- add a graphical way (animated plot) to see visualize attack.

## Running

First, execute Docker (on Windows, you must open Docker Desktop).

Then, go to project's root directory (where the `docker-compose.yml` file is) and run on terminal:

- `docker compose up`

## Install Poetry (for dev)

- https://python-poetry.org/docs/#installing-with-the-official-installer

After installing `poetry`, run on terminal:

- `poetry install`
- `pre-commit install`

## References

- Python Sockets (TCP): https://realpython.com/python-sockets/
