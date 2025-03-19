import logging
from datetime import datetime

from simulation_app import SimulationApp

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app = SimulationApp()
    app.run()