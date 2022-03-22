from robot import Robot
from weapon import Weapon 

class Fleet:
    def __init__(self):
        self.robots = []
    def robo1(self):
        weapon1 = Weapon('Laser', 25)
        robot1 = Robot('CY the Cyborg', 50, weapon1)
        self.robots.append(robot1)
    def robo2(self):  
        weapon2 = Weapon('Freeze Ray', 10)
        robot2 = Robot('Ty the Titan', 75, weapon2)
        self.robots.append(robot2)
    