class Dinosaur:
    def __init__(self, name, health, attackpower):
        self.dinosaur_name = name
        self.dinosaur_health = health
        self.attackpower = attackpower

    def dino_attack(self, robot):
        robot.health = robot.health - self.attackpower
        print(robot.health)
        