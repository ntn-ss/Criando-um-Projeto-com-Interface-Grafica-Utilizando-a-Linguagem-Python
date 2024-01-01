class Funcionario:
    "Isto é a docstring da classe 'Funcionário'."
    
    def __init__(self, nome, email):
        self.nome=nome
        self.email = email
        self.horas = {}
        self.salario_hora={}
    
    def cadastro_hora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas
            
    def cadastro_salario_hora(self, mes, valor):
        if (mes not in self.salario_hora):
            self.salario_hora[mes] = valor
        
    def calcula_salario(self, mes):
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print('Mês inexistente.')
        else:
            return f'Pagamento em {mes}: {self.horas[mes] * self.salario_hora[mes]}.\n'
    def __repr__(self):
        print('----- Pagamentos mensais -----'.upper())
        for mes in self.horas:
            print(self.calcula_salario(mes))
        return f'\n----------------------------------------\nFuncionário: {self.nome},\nE-mail: {self.email},\nHoras/mês: {self.horas},\nSalário/hora: {self.salario_hora}\n----------------------------------------\n'