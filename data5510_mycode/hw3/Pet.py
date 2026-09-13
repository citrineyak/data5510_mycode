class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_species(self, species):
        self.species = species
    def calc_human_age(self):
        return self.age * 7
    def avg_lifespan(self):
        lifespans = {
            "dog": 12,
            "cat": 15,
            "rabbit": 10,
            "hamster": 3,
            "bird": 10
        }
        return lifespans.get(self.species.lower(), "Unknown Species")

p1 = Pet("Doggo", 5)
p2 = Pet("Bunny", 3)
p3 = Pet("Birdo", 6)

p1.set_species("dog")
p2.set_species("rabbit")
p3.set_species("bird")
print("Human Ages")
print(p1.calc_human_age())
print(p2.calc_human_age())
print(p3.calc_human_age())
print("\n")
print("Average Lifespans")
print(p1.avg_lifespan())
print(p2.avg_lifespan())
print(p3.avg_lifespan())
