from model import EcosystemModel

model = EcosystemModel(10, 10, 20)

for i in range(20):
    model.step()
    print("Step", i)