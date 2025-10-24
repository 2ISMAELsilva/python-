import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class cliente:
    nome: str
    cpf: str
    telefone: str
    
    # função da classe
    def dados_dos_clientes(self):
        print(f'\nNome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Telefone: {self.telefone}')
        
    def dados_marketing(self):
        print(f"Telefone: {self.telefone}")
        
vetor_clientes = []


for i in range(3):
    os.system("cls")
    dados_clientes = cliente(nome=input('Informe seu nome: '),
                             cpf=input('Informe seu CPF: '),
                             telefone=input('Agora informe o seu Telefone: '))
    vetor_clientes.append(dados_clientes)
    
print("=== Mostrando dados ===")
for dados_clientes in vetor_clientes:
    dados_clientes.dados_dos_clientes()
    
print("\n=== dados marketing ===")
for dados_clientes in vetor_clientes:
    dados_clientes.dados_marketing()

    
