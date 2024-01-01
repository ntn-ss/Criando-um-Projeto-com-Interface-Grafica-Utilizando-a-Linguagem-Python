class Pessoa:
    "Isto é a docstring da classe 'Pessoa'."
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        print(f'Oi, eu sou {self.nome} e tenho {self.idade} anos.')