class Dinosaur:
    def __init__(self, name):
        self.dinosaur_name = name
        self.dinosaur_health = None
        self.attackpower = None

    def dino_attack(self, robo):
        print(f'{self.dinosaur_name} attacks {robo.name} with his chompers!')
