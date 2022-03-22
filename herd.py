from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
    def dinoss(self):
        dino1 = Dinosaur('Tex the T-REX', 80, 30)
        self.dinosaurs.append(dino1)
        dino2 = Dinosaur('Ry the Raptor', 50, 20)
        self.dinosaurs.append(dino2)
    def dino_attack(self):
        print('Tex the T-REX does some wicked damage with his tail smash!')
        print('Ry the Raptor uses his speed dash to slam into the robots!')
        

            

        
