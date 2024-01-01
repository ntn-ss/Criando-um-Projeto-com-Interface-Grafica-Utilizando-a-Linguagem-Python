import math
from Azulejo import Azulejo

class Piso:
    "Isto é a docstring da classe 'Piso'"
    
    def __init__(self, azulejo: Azulejo, largura, altura):
        self.azulejo = azulejo
        self.largura = largura
        self.altura = altura
        
    def __repr__(self):
        return f'Este piso tem largura de {self.largura} m e altura de {self.altura} m.'
        
    def calculaArea(self):
        return self.largura * self.altura
    
    def trocaAzulejo(self, azulejoNovo: Azulejo):
        self.azulejo = azulejoNovo if (azulejoNovo != self.azulejo) else print('O azulejo deve ser outro.')
    
    def calculaAzulejos(self):
        quantidadeAzulejos = self.calculaArea()/self.azulejo.calcula_area()
        
        if (self.calculaArea() % self.azulejo.calcula_area() == 0):
            return f'Azulejos necessários para preencher o piso: {quantidadeAzulejos}.'
        else:
            return f'Mínimo de azulejos necessários para preencher o piso: {math.ceil(quantidadeAzulejos)}.'