from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_battle(self):
        self.welcome()
        self.welcome_bots()
        self.welcome_dino()
        self.dino_turn()
        self.robo_turn()
        self.the_winner()
        
    def welcome(self):  
        print('Welcome to the 1st Annual Time Battle! Robots VS Dinosaurs! Enjoy!')
    def welcome_bots(self):
        print(f'Welcome {robo1} and {Fleet.robo2} to the Battefield!') 
    def welcome_dino(self):
        print(f'Welcome {Herd.dinosaur1} and {Herd.dinosaur2} to the Battefield!')
    def dino_turn(self):
        self.dinogo = Dinosaur.dino_attack
        print(self.dinogo)
    def robo_turn(self):
        self.botgo = robot_attack
        print(self.botgo)
    def the_winner(self):
        if self.herd.dinosaurs == 0:
            print('The robots have won!')
        elif self.fleet.robots == 0:
            print('The Dinosaurs have won!')
        else:
            print('Wow, its a draw!')
        
        
       
    
    


