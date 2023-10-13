class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

class ContaInvestimento(ContaBancaria):
    def __init__(self, saldo_inicial, taxa_juros):
        super().__init__(saldo_inicial)
        self.taxa_juros = taxa_juros

    def adicioneJuros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros