from mesa import Agent

class AnimalAgent(Agent):
    def __init__(self, unique_id, model, animal_type):
        super().__init__(unique_id, model)
        self.type = animal_type

    def step(self):
        # simple random movement
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)