from robot import Robot
from weapon import Weapon 

class Fleet:
    def __init__(self):
        self.robots = []
    def robotss(self):
        weapon1 = Weapon('Laser', 25)
        weapon2 = Weapon('Freeze Ray', 10)
        robot1 = Robot('CY the Cyborg', 50, weapon1)
        self.robots.append(robot1)
        robot2 = Robot('Ty the Titan', 75, weapon2)
        self.robots.append(robot2)
    def robot_attack(self):
        print('Cy the cyborg uses his Laser vison, and does some serious damage!')
        print('Ty follows up from Cys attack with his freeze ray! That was cold!')
        
        
    