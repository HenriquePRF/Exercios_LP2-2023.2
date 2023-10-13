class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentarSalario(self, porcentual_de_aumento):
        aumento = (porcentual_de_aumento / 100) * self.salario
        self.salario += aumento

# Programa de teste

nome_funcionario = input("Digite o nome do funcionário: ")
salario_funcionario = float(input("Digite o salário do funcionário: "))

funcionario = Funcionario(nome_funcionario, salario_funcionario)

print(f"Nome do funcionário: {funcionario.obter_nome()}")
print(f"Salário do funcionário: R${funcionario.obter_salario():.2f}")

# Aumentar o salário em 10%
porcentual_de_aumento = float(input("Digite o porcentual de aumento do salário: "))
funcionario.aumentarSalario(porcentual_de_aumento)

print(f"Novo salário do funcionário: R${funcionario.obter_salario():.2f}")
