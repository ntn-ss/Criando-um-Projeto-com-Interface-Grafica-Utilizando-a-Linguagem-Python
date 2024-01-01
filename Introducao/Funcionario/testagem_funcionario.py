from Funcionario import Funcionario

fulano = Funcionario('Fulano', 'fulanitodetal@gmail.com')

fulano.cadastro_hora('Jan', 300)
fulano.cadastro_hora('Fev', 200)

fulano.cadastro_salario_hora('Jan', 30)
fulano.cadastro_salario_hora('Fev', 30)

print(fulano)

fulano.cadastro_hora('Mar', 500)
fulano.cadastro_salario_hora('Mar', 50)
print(fulano.calcula_salario('Mar'))

print(fulano)