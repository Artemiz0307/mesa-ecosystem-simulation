from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from model import EcosystemModel


def agent_portrayal(agent):

    portrayal = {
        "Shape": "circle",
        "Color": "blue",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5
    }

    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = ModularServer(
    EcosystemModel,
    [grid],
    "Ecosystem Simulation",
    {"width": 10, "height": 10, "num_agents": 20}
)

server.port = 8521
server.launch()