from mesa import Agent


class Prey(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()

        # reproduction chance
        if self.random.random() < 0.04:
            new_prey = Prey(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_prey, self.pos)
            self.model.schedule.add(new_prey)


class Predator(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = 5

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def eat(self):

        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        prey = [agent for agent in cellmates if isinstance(agent, Prey)]

        if len(prey) > 0:
            victim = self.random.choice(prey)

            self.model.grid.remove_agent(victim)
            self.model.schedule.remove(victim)

            self.energy += 5

    def step(self):

        self.move()
        self.energy -= 1

        self.eat()

        if self.energy <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)

        # reproduction
        if self.random.random() < 0.02:
            child = Predator(self.model.next_id(), self.model)
            self.model.grid.place_agent(child, self.pos)
            self.model.schedule.add(child)