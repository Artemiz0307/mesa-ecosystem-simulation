# Mesa Ecosystem Simulation

A simple **agent-based ecosystem simulation** built using the **Mesa framework** for Python.
This project demonstrates how autonomous agents interact within a grid environment and how complex behaviors can emerge from simple rules.

The repository was created as a learning project to explore **agent-based modeling (ABM)** and understand how the Mesa framework structures simulations.

---

## What is Agent-Based Modeling?

Agent-Based Modeling (ABM) is a simulation technique used to model systems made of **independent interacting agents**. Each agent follows simple rules, but their interactions can produce complex and emergent behaviors.

ABM is widely used in:

* ecology
* economics
* social science
* epidemiology
* urban planning
* artificial intelligence research

---

## About Mesa

Mesa is an **open-source Python library** for agent-based modeling that allows developers and researchers to build simulations of complex systems.

Mesa provides tools for:

* creating autonomous agents
* managing simulation environments
* scheduling agent behavior
* collecting simulation data
* visualizing simulations in a web browser

Official documentation:
https://mesa.readthedocs.io

---

## Project Overview

This simulation models a simple ecosystem where agents move randomly on a grid.

Each agent:

* occupies a position in the environment
* moves randomly at each simulation step
* is scheduled by the simulation engine

Although simple, this model demonstrates the **core structure of Mesa simulations**.

The goal of this project is to understand how Mesa organizes:

* agents
* environments
* schedulers
* simulation loops

---

## Project Structure

```
mesa-ecosystem-simulation
│
├── agent.py      # Defines agent behavior
├── model.py      # Defines the ecosystem model
├── run.py        # Runs the simulation
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/Artemiz0307/mesa-ecosystem-simulation.git
cd mesa-ecosystem-simulation
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment.

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

Install dependencies:

```
pip install mesa==1.2.1
```

---

## Running the Simulation

Run the simulation using:

```
python run.py
```

The model will run several steps and simulate agents moving across the grid.

Example output:

```
Step 1
Step 2
Step 3
Step 4
...
```

---

## Learning Goals

This project explores:

* fundamentals of agent-based modeling
* Mesa framework architecture
* simulation design in Python
* grid environments and scheduling
* emergent behaviors from simple rules

---

## Possible Improvements

Future enhancements for the simulation could include:

* predator-prey dynamics
* resource consumption
* agent reproduction
* environmental constraints
* graphical visualization
* data collection and analysis

---

## Contributing

Contributions are welcome.

If you want to improve the simulation or experiment with new agent behaviors, feel free to:

1. fork the repository
2. create a feature branch
3. submit a pull request

---

## License

This project is open-source and available under the **MIT License**.
