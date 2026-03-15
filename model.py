from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from agent import AnimalAgent


class EcosystemModel(Model):

    def __init__(self, width=10, height=10, num_agents=20):

        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        for i in range(num_agents):

            agent = AnimalAgent(i, self, "animal")

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)
    def step(self):
        self.schedule.step()