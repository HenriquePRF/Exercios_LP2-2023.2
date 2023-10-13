class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def digerir(self):
        if len(self.bucho) > 0:
            print(f"{self.nome} está digerindo {', '.join(self.bucho)}.")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada no bucho para digerir.")

    def verBucho(self):
        print(f"O bucho do {self.nome} contem: {', '.join(self.bucho)}")

# Criando dois macacos
macaco1 = Macaco("Macaco1")
macaco2 = Macaco("Macaco2")

# Alimentando os macacos
macaco1.comer("banana")
macaco2.comer("maçã")
macaco1.comer("laranja")

# Verificando o conteúdo do estômago
macaco1.verBucho()
macaco2.verBucho()

# Digerindo o que está no estômago
macaco1.digerir()
macaco2.digerir()

# Tentando fazer um macaco comer o outro
macaco1.comer("macaco2")

# Verificando o conteúdo do estômago novamente
macaco1.verBucho()
macaco2.verBucho()