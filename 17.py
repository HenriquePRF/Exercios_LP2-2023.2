import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)

    def alimentar(self):
        self.fome -= random.randint(10, 30)
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.tedio -= random.randint(10, 30)
        if self.tedio < 0:
            self.tedio = 0

    def ouvir(self):
        print(f"{self.nome}: Estou feliz!")

    def estado(self):
        print(f"{self.nome}: Fome = {self.fome}, Tédio = {self.tedio}")

# Criar uma fazenda de bichinhos
fazenda = []

# Adicionar alguns bichinhos à fazenda
nomes_bichinhos = ["Bichinho1", "Bichinho2", "Bichinho3"]
for nome in nomes_bichinhos:
    bichinho = Bichinho(nome)
    fazenda.append(bichinho)

# Menu
while True:
    print("\nAções para a fazenda de bichinhos:")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Ver estado de todos os bichinhos")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        for bichinho in fazenda:
            bichinho.alimentar()
    elif escolha == "2":
        for bichinho in fazenda:
            bichinho.brincar()
    elif escolha == "3":
        for bichinho in fazenda:
            bichinho.ouvir()
    elif escolha == "4":
        for bichinho in fazenda:
            bichinho.estado()
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
