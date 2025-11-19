import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")
        print("-" * 40)


def salvar_em_csv(lista, nome_arquivo="Funcionarios.csv"):
    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        for f in lista:
            arq.write(f"{f.nome},{f.data_nascimento},{f.rg},{f.cpf}\n")
    print("\nDados salvos com sucesso!")


def ler_arquivo(nome_arquivo="Funcionarios.csv"):
    funcionarios = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()

            for linha in linhas:
                nome, data_nasc, rg, cpf = linha.strip().split(",")
                funcionario = Funcionario(nome, data_nasc, rg, cpf)
                funcionarios.append(funcionario)

    except FileNotFoundError:
        print("Arquivo não encontrado!")

    return funcionarios


lista_funcionarios = []
QUANTIDADE = 5

print("Cadastro de Funcionários:\n")

for i in range(QUANTIDADE):
    print(f"Funcionário {i + 1}:")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    rg = input("RG: ")
    cpf = input("CPF: ")

    funcionario = Funcionario(nome, data_nascimento, rg, cpf)
    lista_funcionarios.append(funcionario)

    print()

# Salvar no arquivo
salvar_em_csv(lista_funcionarios)

# Ler e exibir
print("\nFuncionários cadastrados no arquivo:")
funcs = ler_arquivo()

for f in funcs:
    f.exibir()
