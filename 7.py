class Tamagushi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.saude = 100
        self.idade = 0
    
    def mudar_nome(self, novo_nome):
        self.nome = novo_nome

    def mudar_idade(self, nova_idade):
        self.idade = nova_idade

    def mudar_saude(self, nova_Saude):
        self.saude = nova_Saude
    
    def mudar_fome(self, nova_fome):
        self.fome = nova_fome

    def retornar_nome(self):
        return self.nome 

    def retornar_idade(self):
        self.idade 

    def retornar_saude(self):
        self.saude 
    
    def retornar_fome(self):
        self.fome 
    
    def retornar_humor(self):
        return (self.fome + self.saude)/2

    
