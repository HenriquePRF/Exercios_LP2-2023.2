class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Ponto: ({self.x}, {self.y})')

class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial

    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)

def criar_retangulo():
    largura = float(input('Digite a largura do retângulo: '))
    altura = float(input('Digite a altura do retângulo: '))
    x_inicial = float(input('Digite a coordenada x do ponto inicial: '))
    y_inicial = float(input('Digite a coordenada y do ponto inicial: '))
    ponto_inicial = Ponto(x_inicial, y_inicial)
    retangulo = Retangulo(largura, altura, ponto_inicial)
    centro = retangulo.encontrar_centro()
    print(f'Centro do retângulo: ({centro.x}, {centro.y})')

while True:
    print("\nMENU:")
    print("1. Criar Retângulo e mostrar seu centro")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        criar_retangulo()
    elif escolha == '2':
        break
    else:
        print("Opção inválida. Tente novamente.")
