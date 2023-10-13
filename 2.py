class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarLado(self, novo_lado):
        self.tamanho_lado = novo_lado

    def retornarLado(self):
        return self.tamanho_lado

    def calcularArea(self):
        return self.tamanho_lado * self.tamanho_lado
