from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run_game(self):
        self.display_welcome()
        self.battle()
        print("**********************************************************************************************************************************************\n")
        self.display_winners()

    def display_welcome(self):
        print("**********************************************************************************************************************************************\n")
        print("ITTTTTSSSS TIMMMMMMMMMMMMMMMMMEEEEEE!!!\n")
        print("Today we have a great battle!\n")
        print("Robots VS Dinosaurs!\n")
        print("**********************************************************************************************************************************************\n")

    def battle(self):
        
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
            self.dino_turn()
            if len(self.fleet.robots) > 0:
                self.robo_turn()

    def dino_turn(self):
        print("\nBelow is a list of Dinos!: ")
        self.show_dino_opponent_options()
        chosen_dino = int(input("\nWhich Dino?: "))

        print("\nChoose the robot who will defend:")
        self.show_robo_opponent_options()
        chosen_robot = int(input("\nWhich Robot?: "))
        
        self.herd.dinosaurs[chosen_dino].attack_robot(
            self.fleet.robots[chosen_robot])

       
        if self.fleet.robots[chosen_robot].health <= 0:
            print(f"{self.fleet.robots[chosen_robot].name} has died")
            self.fleet.robots.remove(self.fleet.robots[chosen_robot])

    def robo_turn(self):
        print("\nBelow is a list of Robots!: ")
        self.show_robo_opponent_options()
        chosen_robot = int(
            input("\nWhich Robot will go?: "))

        print("\nChoose the dinosaur!:")
        self.show_dino_opponent_options()
        chosen_dino = int(
            input("\nWhich dino?: "))

        
        self.fleet.robots[chosen_robot].attack_dino(
            self.herd.dinosaurs[chosen_dino])

       
        if self.herd.dinosaurs[chosen_dino].health <= 0:
            print(
                f"{self.herd.dinosaurs[chosen_dino].name} was beamed!")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[chosen_dino])

    def show_dino_opponent_options(self):
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f"Press {dino_index} for {dino.name}")
            dino_index += 1

    def show_robo_opponent_options(self):
        robot_index = 0
        for robot in self.fleet.robots:
            print(f"Press {robot_index} for {robot.name}")
            robot_index += 1

    def display_winners(self):
        print("We have a winner!")
        if len(self.fleet.robots) > 0:
            print("Robots win!")
        else:
            print("Dinosaurs win!")
        

        
       
    
    


