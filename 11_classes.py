import os
from dataclasses import dataclass
# Limpa a tela (no Windows)

@dataclass
class cliente:
    nome: str
    idade: str
    peso: float
    altura: int
    
    # função da classe
    def dados_dos_clientes(self):
        print(f'\nNome: {self.nome}')
        print(f'CPF: {self.idade}')
        print(f'Telefone: {self.peso}')
        print(f'Telefone: {self.altura}')
        
        
vetor_clientes = []


for i in range(4):
    os.system("cls")
    dados_clientes = cliente(nome=input('Informe seu nome: '),
                             idade=input('Informe sua idade: '),
                             peso=input('Infome seu peso: ' ), 
                             altura=input('infome a sua Altura: '))
    vetor_clientes.append(dados_clientes)


print('===== Moatrando Dados =====')     
for dados_clientes in vetor_clientes:
    dados_clientes.dados_dos_clientes()                            
    
