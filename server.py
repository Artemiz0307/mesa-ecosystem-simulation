from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from model import EcosystemModel
from agent import Predator, Prey


def agent_portrayal(agent):

    if isinstance(agent, Prey):
        return {
            "Shape": "circle",
            "Color": "green",
            "Filled": "true",
            "Layer": 0,
            "r": 0.5
        }

    if isinstance(agent, Predator):
        return {
            "Shape": "circle",
            "Color": "red",
            "Filled": "true",
            "Layer": 1,
            "r": 0.7
        }


grid = CanvasGrid(agent_portrayal, 20, 20, 600, 600)

server = ModularServer(
    EcosystemModel,
    [grid],
    "Predator Prey Simulation",
    {}
)

server.port = 8521

server.launch()