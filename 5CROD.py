import os 
import time
from dataclasses import dataclass
os.system('cls / clear') #Limpar o terminal

lista_clientes = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    
    def mostrar_dados(self):
        print(f'Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}')
        
# Função para erificar se a lista esta vazia
def vereficar_lista_vazia(lista_clientes):
    if not lista_clientes:
        print('\nNão ha clientes cadatrados. ')
        return True
    return False
# função adicionar novo cliente
def adicionar_clientes(lista_clientes):
    print('\nAdicionar novo cliente')
    nome = input('Digite seu nome: ')
    email = input('Digite o seu email: ')
    telefone = input('Digite o seu telefone: ')
    
    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f'Cliente {nome} adicionado com sucesso!!')       
        
# Função para encontrar um cliente na lista.
def encontrar_cliente_por_email(lista_clientes, email_buscar):
    email_buscar_lower = email_buscar.lower()
    for cliente in lista_clientes:
        if cliente.email.lower() == email_buscar_lower:
            return cliente
        return None 

# Função para mostrar todos os clientes
def mostrar_todos_clientes(lista_clientes):
    if vereficar_lista_vazia(lista_clientes):
     return
    
    print('\n--- lista de clientes ---')
    for cliente in lista_clientes:
        cliente.mostrar_dados()
        
# Função para atualizar clientes
def atulizar_clientes(lista_clientes):
    if vereficar_lista_vazia(lista_clientes):
        return
    
    # mostrar lista para ajudar o usuario
    mostrar_todos_clientes(lista_clientes)
    print('=== Stualizar dados dos clientes ===')
    email_buscar = input('\nDigite o E-mail do cliente: ')
    cliente_para_atualizar = encontrar_cliente_por_email(lista_clientes, email_buscar)
    
    if cliente_para_atualizar:
        print("\nPessoa encontrada")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual. ")
        
        print(f'\nNome atual: {cliente_para_atualizar.nome}')
        novo_nome = input('Novo nome: ')
        
        print(f'\nE-mail: {cliente_para_atualizar.email}')
        novo_email = input('NovoE-mail: ')
        
        print(f'\nTelefone: {cliente_para_atualizar.telefone}')
        novo_telefone = input('Novo Telefone: ')
        
        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone
            
        print(f'\nDados do cliente: {email_buscar} atualizados com sucesso!!')
    else:
        print(f'Cliente com E-mail: {email_buscar} não encontrado. ')
        
# Função para excluir um cliente
def  excluir_cliente(lista_cliente): 
    if vereficar_lista_vazia(lista_cliente):
        return
    
    mostrar_todos_clientes(lista_clientes)
    
    email_buscar = input('Digite o E-mail do usuario que deseja buscar: ')
    
    cliente_para_remover = encontrar_cliente_por_email(lista_clientes, email_buscar)
    
    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f'\nCliente com nome: {email_buscar}')        

# moatrar menu
while True:
    print("""
    === Gerenciador de clientes ===      
        1- Adicionar
        2- mostrar todos
        3-Atualizar
        4- Excluir
        5- Sair
                """)
    
    # caso o usuario digite letras
    try:
        opcao = int(input('Digite qual opção deseja: '))
    except ValueError:
        print('\nEntrada Invalida, Digite numeros. ')
        
    match opcao:
        case 1:
            adicionar_clientes(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atulizar_clientes(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        case 0:
            print('\nSaindo do programa... ')
        case _:
            print('\n Opção invalida')
            
    if opcao != 1 and opcao != 0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)
        
    if opcao != 0:
        os.system('cls // clear')
        
        




