class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

# Programa de teste
nome_funcionario = input("Digite o nome do funcionário: ")
salario_funcionario = float(input("Digite o salário do funcionário: "))

funcionario = Funcionario(nome_funcionario, salario_funcionario)

print(f"Nome do funcionário: {funcionario.obter_nome()}")
print(f"Salário do funcionário: R${funcionario.obter_salario():.2f}")
