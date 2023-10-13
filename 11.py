class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.tanque = 0
    
    def andar(self, distancia):
        self.tanque -= distancia/self.consumo

    def obterGasolina(self):
        return self.tanque

    def adicionarGasolina(self, incremento):
        self.tanque += incremento




meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.