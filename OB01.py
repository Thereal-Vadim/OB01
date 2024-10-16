class Warrior():
    def __init__(self, name, power, stamina, hair_color):
        self.name = name
        self.power = power
        self.stamina = stamina
        self.hair_color = hair_color

    def walk(self):
        print(f"{self.name} Walking...")
        self.stamina -= 1

    def sleeping(self):
        print(f"{self.name} Sleeping...")
        self.stamina += 2

    def eat(self):
        print(f"{self.name} Eating...")
        self.power+= 1

    def punch(self):
        print(f"{self.name} Punching...")
        self.stamina -= 2

    def info(self):
        print(f"Warrior Name: {self.name}")
        print(f"Stamina: {self.stamina}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Power: {self.power}")

