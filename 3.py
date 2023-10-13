class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

