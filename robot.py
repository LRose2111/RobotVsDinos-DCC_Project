

from weapon import Weapon


class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon

       
    def robot_attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attackpwr 
        print(dinosaur.health)
    