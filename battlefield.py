from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dino_one = None
        self.robot_one = None
   
    def greeting(self):
        print('Welcome to the 1st Annual Warrior War! For this exclusive event today, we have Rex the T-Rex, and Cy the Cyborg! Enjoy this event, because it will go down in history!')
    def dino_name(self):
        self.dino_one = 'Rex'
        print('First we introduce our contestant in the prehistoric corner! Standing at 40 Feet, and the arm reach of baby arms! Lets hear it for....... REX!')
    def robo_name(self):
        self.robot_one = 'CY'
        print('Last but not least, The One Eyed Wonder, Steel Can Man,.......... Cy the Cyborg!')
    def dino_turn(self):
        self.dino_turn = Dinosaur.dino_attack
    def robo_turn(self):
        self.robo_turn = Robot.robot_attack
    def the_winner(self):
        print('Despite the overwhelming size diffence, CYs steel frame shattered all Rexs teeth, leaving him defenseless to the lasers of CY. The victor is the Steel Can Man CY the Cyborg!')

    
    def run_battle():
        self.greeting()
        self.dino_name()
        self.robo_name()
        self.dino_turn()
        self.robo_turn()
        self.the_winner()

