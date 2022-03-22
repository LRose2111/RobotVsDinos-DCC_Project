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
        self.dino_turn()
        self.robo_turn()
        self.the_winner()
        
    def welcome(self):  
        print('Welcome to the 1st Annual Time Battle! Robots VS Dinosaurs! Enjoy!')
    def welcome_bots(self):
        print(f'In the left corner we have the Robots!') 
    def welcome_dino(self):
        print(f'In the right corner we have the Dinosaurs!')
    def dino_turn(self):
        print('wow, the first strike goes to the Dinosaurs!')
        print(self.herd.dino_attack())

    def robo_turn(self):
        print('The robots strike back!')
        print (self.fleet.robot_attack())
        
    def the_winner(self):
        user_input = input(f'Did you enjoy that epic show down!?'  )
        print('Lets see who the winners are.')
        print('Despite the overwhelming size diffence the Dinosaurs had, the Robots proved that the future is overpowered!')
        print('Robots Win!!!!!!!!!!!!!')
        print('Thank you for attending the 1ST ever Time Battle! We will see you next year!')
            
        
        

        
       
    
    


