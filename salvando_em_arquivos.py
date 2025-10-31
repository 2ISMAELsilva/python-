import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: int

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome= input("Infome seu nome: "),
        idade= int(input("Infome sua idade: ")),
        email= input('Informe seu E-mail: '),
        telefone= int(input('Infome seu telefone: '))
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_aluno.txt"

with open(arquivo, "w") as arquivo_aluno:
    for aluno in lista_alunos:
        arquivo_aluno.write(f"{aluno.nome},{aluno.idade},{aluno.email} {aluno.telefone}\n")
    print("salvo com sucesso!")
