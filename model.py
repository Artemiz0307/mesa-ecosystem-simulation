from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agent import Predator, Prey


class EcosystemModel(Model):

    def __init__(self, width=20, height=20, initial_prey=40, initial_predators=10):

        super().__init__()

        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # create prey
        for i in range(initial_prey):

            prey = Prey(self.next_id(), self)

            x = self.random.randrange(width)
            y = self.random.randrange(height)

            self.grid.place_agent(prey, (x, y))
            self.schedule.add(prey)

        # create predators
        for i in range(initial_predators):

            predator = Predator(self.next_id(), self)

            x = self.random.randrange(width)
            y = self.random.randrange(height)

            self.grid.place_agent(predator, (x, y))
            self.schedule.add(predator)

    def step(self):
        self.schedule.step()