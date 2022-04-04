from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        ry = Dinosaur('RY', 60)  
        self.dinosaurs.append(ry)

        rex = Dinosaur('Rex', 60) 
        self.dinosaurs.append(rex)

       
        

            

        
