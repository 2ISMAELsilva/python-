import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: str

QUANTIDADE_DE_LIVROS = 4
lista_livros = []

print("Solicitando dados dos livros")
for i in range(QUANTIDADE_DE_LIVROS):
    livro = Livro(
        nome= input("Infome o nome do Livro: "),
        autor= (input("Infome o autor do livro: ")),
        categoria= input('Informe a categoria do livro: '),
        preco= (input('Infome o Preço do livro: '))
    )
    lista_livros.append(livro)

print()
print("Salvando dados.")
arquivo = "catalogo_livros.txt"

with open(arquivo, "w") as arquivo_aluno:
    for aluno in lista_livros:
        arquivo_aluno.write(f"{livro.nome},{livro.autor},{livro.categoria} {livro.preco}\n")
    print("salvo com sucesso!")
