class Tamagushi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.saude = 100
        self.idade = 0
        self.tedio = 100

    def mudar_nome(self, novo_nome):
        self.nome = novo_nome

    def mudar_idade(self, nova_idade):
        self.idade = nova_idade

    def mudar_saude(self, nova_saude):
        self.saude = nova_saude

    def mudar_fome(self, nova_fome):
        self.fome = nova_fome

    def retornar_nome(self):
        return self.nome

    def retornar_idade(self):
        return self.idade

    def retornar_saude(self):
        return self.saude

    def retornar_fome(self):
        return self.fome

    def retornar_humor(self):
        return (self.fome + self.saude) / 2

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def __str__(self):
        return f"{self.nome}:\nFome: {self.fome}\nTédio: {self.tedio}\nSaúde: {self.saude}\nIdade: {self.idade}"

# Programa de teste
if __name__ == "__main__":
    nome_tamagushi = input("Digite o nome do seu Tamagushi: ")
    tamagushi = Tamagushi(nome_tamagushi)

    while True:
        print(f"\n{tamagushi.retornar_nome()}:")
        print(f"Fome: {tamagushi.retornar_fome()}")
        print(f"Tédio: {tamagushi.tedio}")
        print(f"Saúde: {tamagushi.retornar_saude()}")
        print(f"Idade: {tamagushi.retornar_idade()}")
        print(f"Humor: {tamagushi.retornar_humor()}")

        acao = input("\nO que você quer fazer? (alimentar, brincar, veratributos, sair): ")

        if acao == "alimentar":
            quantidade_comida = int(input("Quantidade de comida a fornecer: "))
            tamagushi.alimentar(quantidade_comida)
        elif acao == "brincar":
            tempo_brincadeira = int(input("Tempo de brincadeira: "))
            tamagushi.brincar(tempo_brincadeira)
        elif acao == "veratributos":
            print(tamagushi)  # Ação secreta para ver todos os atributos
        elif acao == "sair":
            break
        else:
            print("Ação inválida. Tente novamente.")
