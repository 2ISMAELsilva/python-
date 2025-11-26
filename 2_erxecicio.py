import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco: str
    
    def exibir(self):
        print(f'\n--- Funcionário ---')
        print(f'Nome: {self.nome}')
        print(f'Data de admissão: {self.data_admissao}')
        print(f'Matrícula: {self.matricula}')
        print(f'Endereço: {self.endereco}')

@dataclass
class Cliente:
    nome: str
    data_nascimento: str
    endereco: str
    
    def exibir(self):
        print(f'\n--- Cliente ---')
        print(f'Nome: {self.nome}')
        print(f'Nascimento: {self.data_nascimento}')
        print(f'Endereço: {self.endereco}')


# -----------------------------
# Funções pedidas no exercício
# -----------------------------

def mostrar_funcionarios(lista):
    print("\n===== LISTA DE FUNCIONÁRIOS =====")
    for f in lista:
        f.exibir()

def mostrar_clientes(lista):
    print("\n===== LISTA DE CLIENTES =====")
    for c in lista:
        c.exibir()



# Entrada de dados

FUNCIONARIOS = 3
CLIENTES = 3

vetor_funcionarios = []
vetor_clientes = []

# Cadastro funcionários
for i in range(FUNCIONARIOS):
    print(f"\nCadastro do funcionário {i+1}:")
    f = Funcionario(
        nome=input("Nome: "),
        data_admissao=input("Data de admissão: "),
        matricula=input("Matrícula: "),
        endereco=input("Endereço: ")
    )
    vetor_funcionarios.append(f)

# Cadastro clientes
for i in range(CLIENTES):
    print(f"\nCadastro do cliente {i+1}:")
    c = Cliente(
        nome=input("Nome: "),
        data_nascimento=input("Data de nascimento: "),
        endereco=input("Endereço: ")
    )
    vetor_clientes.append(c)



# Salvando nos arquivos CSV

with open("Dados_funcionarios.csv", "w") as arq_func:
    for f in vetor_funcionarios:
        arq_func.write(f"{f.nome};{f.data_admissao};{f.matricula};{f.endereco}\n")

with open("Dados_clientes.csv", "w") as arq_cli:
    for c in vetor_clientes:
        arq_cli.write(f"{c.nome};{c.data_nascimento};{c.endereco}\n")

print("\nArquivos salvos com sucesso!")



# Exibindo dados na tela

mostrar_funcionarios(vetor_funcionarios)
mostrar_clientes(vetor_clientes)
