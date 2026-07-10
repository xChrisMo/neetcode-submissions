class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health

# TODO: Create Superhero instances
bat_man = SuperHero('Batman', 'Intelligence', 100)
super_man = SuperHero('Superman', 'Strength', 150)

# TODO: Print out the attributes of each superhero
print(bat_man.name)
print(bat_man.power)
print(bat_man.health)


print(super_man.name)
print(super_man.power)
print(super_man.health)