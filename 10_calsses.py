import os
from dataclasses import dataclass

# Limpa a tela (no Windows)
os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str


@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def dados_dos_clientes(self):
        print(f"\n--- Dados do Cliente ---")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, {self.endereco.numero} - {self.endereco.cidade}")


# Solicitando os dados do usuário
print("Cadastro de Cliente\n")

nome = input("Informe seu nome: ")
email = input("Informe seu e-mail: ")
logradouro = input("Informe o logradouro: ")
numero = int(input("Informe o número: "))
cidade = input("Informe a cidade: ")

# Criando o objeto Endereco
endereco_cliente = Endereco(logradouro, numero, cidade)

# Criando o objeto Cliente
dados_cliente = Cliente(nome, email, endereco_cliente)

# Exibindo os dados
dados_cliente.dados_dos_clientes()

        
        
        
    