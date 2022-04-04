from robot import Robot
from random import random

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        cy = Robot('CY')
        self.robots.append(cy)

        spock = Robot('Spock')
        self.robots.append(spock)

        

        
    