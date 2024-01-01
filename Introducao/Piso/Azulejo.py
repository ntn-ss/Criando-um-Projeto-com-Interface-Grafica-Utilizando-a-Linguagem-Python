class Azulejo:
    "Isto é a docstring da classe 'Azulejo'"
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def __repr__(self):
        return f'Este azulejo tem base de {self.base} cm e altura de {self.altura} cm.'
        
    def calcula_area(self):
        return self.base * self.altura / 100 # Lembre-se: está em centímetros