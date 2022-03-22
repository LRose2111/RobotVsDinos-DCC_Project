from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_battle(self):
        self.welcome()
        self.welcome_bots()
        self.welcome_dino()
        
    def welcome(self):  
        print('Welcome to the 1st Annual Time Battle! Robots VS Dinosaurs! Enjoy!')
    def welcome_bots(self):
        print(f'Welcome {Fleet.robo1} and {Fleet.robo2} to the Battefield!') 
    def welcome_dino(self):
        print(f'Welcome {Herd.dinosaur1} and {Herd.dinosaur2} to the Battefield!')
    def dino_turn(self):
        pass
    def robo_turn(self):
        pass
    def the_winner(self):
        pass
       
    
    


