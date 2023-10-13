class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.5  # Cresce 0,5 cm por ano até 21 anos

    def engordar(self, peso_gordura):
        self.peso += peso_gordura

    def emagrecer(self, peso_perda):
        self.peso -= peso_perda

    def crescer(self, altura_crescimento):
        self.altura += altura_crescimento
