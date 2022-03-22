from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
    
    def dinosaur1(self):
        dino1 = Dinosaur('Tex the T-REX', 80, 30)
        self.dinosaurs.append(dino1)
    def dinosaur2(self):   
        dino2 = Dinosaur('Ry the Raptor', 50, 20)
        self.dinosaurs.append(dino2)
    


        
