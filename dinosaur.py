class Dinosaur:
    def __init__(self, name, attackpwr):
        self.dinosaur_name = name
        self.dinosaur_health = 100
        self.attackpower = attackpwr

    def dino_attack(self, robo):
        robo.health -= 50
        print(f'{self.dinosaur_name} attacks {robo.name} with his chompers!')
