import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.

# cliente e uma pessoa?
# Cpf? endereço? titulo de eleitor? E-mail? telefone?
# Seu sistema precisa de algumas informações.
# Uma venda
# Endereço,Nome,Telefone.(minimundo)



@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str
    
    # Função apenas dessa classe
    def mostrar_dados_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')
        


# Criando dois clientes com as características
# definidas na classe.

lista_de_clientes = []

for i in range(2):
    dados_cliente = Cliente(nome=input('Digite seu nome'),
                    endereco=input('Digite o seu Endereço: '),
                    telefone=input("Digite seu telefone: "))
    lista_de_clientes.append(dados_cliente)

for dados_cliente in lista_de_clientes:
    dados_cliente.mostrar_dados_cliente()