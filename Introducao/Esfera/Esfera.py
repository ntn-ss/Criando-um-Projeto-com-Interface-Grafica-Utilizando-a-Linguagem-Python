import math

class Esfera:
    "Isto é a docstring da classe 'Esfera'."
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
    
    def calcula_area(self):
        ar = 4*math.pi*(self.raio**2)
        print(f'Esta é uma esfera {self.cor} de área {ar:.2f} cm².')
    
    def calcula_volume(self):
        vol = (4/3)*math.pi*(self.raio**3)
        print(f'Esta é uma esfera {self.cor} de volume {vol:.2f} cm³.')