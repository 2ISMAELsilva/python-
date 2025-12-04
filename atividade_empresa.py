import os 
import time
from dataclasses import dataclass

os.system('cls || clear') 

lista_clientes = []
lista_produtos = []

#CLASSES

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados_clientes(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        
        
@dataclass
class Produto:
    nome: str
    quantidade: float
    lote: str
    validade: float

    def mostrar_dados_produtos(self):
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Lote: {self.lote}")
        print(f"Validade: {self.validade}")

# FUNÇÕES 

def verificar_lista_vazia(lista):
    if not lista:
        print("\n❗ Não há clientes cadastrados.")
        return True
    return False

def verificar_lista_vazia2(lista):
    if not lista:
        print("\n❗ Não há produtos cadastrados.")
        return True
    return False

# CADASTRANDO CLIENTES
def adicionar_cliente(lista):
    print("\n---- Adicionando novo Cliente ----")
    nome1 = input("Digite o seu Nome: ")
    email = input("Digite o seu E-mail: ")
    telefone = input("Digite o seu Telefone: ")
    endereco = input("Digite o seu Endereço: ")

    cliente = Cliente(nome1, email, telefone , endereco)

    lista.append(cliente)
    print(f"\n✔ Cliente {nome1} cadastrado com sucesso!\n")
    
    # abrir menu de produtos automaticamente
    menu2()

# CADASTRANDO PRODUTOS
def adicionar_produto(lista):
    print("\n---- Adicionando novo Produto ----")
    nome2 = input("Nome: ")
    quantidade = input("Quantidade: ")
    lote = input("Lote: ")
    validade = input("Validade: ")

    produto = Produto(nome2, quantidade, lote , validade)

    lista.append(produto)
    print(f"\n✔ produto {nome2} cadastrado com sucesso!\n")

# lista clientes
def listar_clientes(lista):
    print("\n--- Lista de clientes Cadastrados ---")
    if verificar_lista_vazia(lista):
        return

    for cliente in lista:
        print("\n------------------------------------")
        cliente.mostrar_dados_clientes()
    print("------------------------------------\n")

# lista produtos
def listar_produtos(lista):
    print("\n--- Lista de Produtos Cadastrados ---")
    if verificar_lista_vazia2(lista):
        return

    for produto in lista:
        print("\n------------------------------------")
        produto.mostrar_dados_produtos()
    print("------------------------------------\n")

# Buscar Cliente pelo nome
def buscar_por_nome1(lista, nome1):
    for cliente in lista:
        if cliente.nome == nome1:
            return cliente
    return None

# Buscar produto peo nome
def buscar_por_nome2(lista, nome2):
    for produto in lista:
        if produto.nome == nome2:
            return produto
    return None

# Atualizando cliente
def atualizar_cliente(lista):
    print("\n--- Atualizar Cliente ---")
    nome = input("Digite o NOME do cliente: ")

    cliente = buscar_por_nome1(lista, nome)
    if cliente is None:
        print("❗ Cliente não encontrado!")
        return

    print("\nDeixe em branco para manter o valor atual.")

    novo_nome = input(f"Nome ({cliente.nome}): ") or cliente.nome
    novo_email = input(f"E-mail ({cliente.email}): ") or cliente.email
    novo_telefone = input(f"Telefone ({cliente.telefone}): ") or cliente.telefone
    novo_endereco = input(f"Endereço ({cliente.endereco}): ") or cliente.endereco

    cliente.nome = novo_nome
    cliente.email = novo_email
    cliente.telefone = novo_telefone
    cliente.endereco = novo_endereco

    print("\n✔ Dados do cliente atualizados com sucesso!\n")

# Excluir cliente
def excluir_cliente(lista):
    print("\n--- Excluir cliente ---")
    nome = input("Digite o nome do Cliente: ")

    cliente = buscar_por_nome1(lista, nome)

    if cliente is None:
        print(" Cliente não encontrado!")
        return

    lista.remove(cliente)
    print("\n Cliente removido com sucesso!\n")

# Atualizando produto
def atualizar_produto(lista):
    print("\n--- Atualizar Produto ---")
    nome = input("Digite o NOME do produto: ")

    produto = buscar_por_nome2(lista, nome)
    if produto is None:
        print("❗ Produto não encontrado!")
        return

    print("\nDeixe em branco para manter o valor atual.")

    novo_nome = input(f"Nome ({produto.nome}): ") or produto.nome
    nova_quantidade = input(f"Quantidade ({produto.quantidade}): ") or produto.quantidade
    novo_lote = input(f"Lote ({produto.lote}): ") or produto.lote
    nova_validade = input(f"Validade ({produto.validade}): ") or produto.validade

    produto.nome = novo_nome
    produto.quantidade = nova_quantidade
    produto.lote = novo_lote
    produto.validade = nova_validade

    print("\n Dados do produto atualizados com sucesso!\n")

# Excluir produto
def excluir_produto(lista):
    print("\n--- Excluir Produto ---")
    nome = input("Digite o nome do Produto: ")

    produto = buscar_por_nome2(lista, nome)

    if produto is None:
        print(" Produto não encontrado!")
        return

    lista.remove(produto)
    print("\n Produto removido com sucesso!\n")

# MENU DE CLIENTES
def menu1():
        print("\n=========== SISTEMA DE CLIENTES ===========")
        print("1 - Adicionar Cliente")
        print("2 - Listar Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Sair")
        print("=============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cliente(lista_clientes)
        elif opcao == "2":
            listar_clientes(lista_clientes)
        elif opcao == "3":
            atualizar_cliente(lista_clientes)
        elif opcao == "4":
            excluir_cliente(lista_clientes)
        elif opcao == "5":
            print("\nEncerrando o sistema...")
            
        else:
            print(" Opção inválida! Tente novamente.")

# MENU DE PRODUTOS
def menu2():
        print("\n=========== SISTEMA DE PRODUTOS ===========")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Excluir Produto")
        print("5 - Sair")
        print("=============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(lista_produtos)
        elif opcao == "2":
            listar_produtos(lista_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos)
        elif opcao == "4":
            excluir_produto(lista_produtos)
        elif opcao == "5":
            print("\nEncerrando o sistema...")
    
        else:
            print(" Opção inválida! Tente novamente.")

menu1()
menu2()
