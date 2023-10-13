class Combustivel:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor_do_litro = valor
        self.quantidade = 100

    def abastecerPorValor(self, valor):
        self.quantidade -= valor/self.valor_do_litro
        return valor/self.valor_do_litro
    
    def abastecerPorLitro(self, litro):
        self.quantidade -= litro
        return litro * self.valor_do_litro
    
    def alterarValor(self, novo_valor):
        self.valor_do_litro = novo_valor
    
    def alterarCombustivel(self, novo_tipo):
        self.tipo = novo_tipo

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade = nova_quantidade

    