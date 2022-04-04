class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack_robot(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name} for {self.attack_power} damage. Their new health is {robot.health}.")
        
        