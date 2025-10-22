import os
from dataclasses import dataclass
os.system('cls')

# Estrutura de dados 
@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: int

@dataclass
class pet:
    nome: str
    idade: int
    peso: float

# Exemplo de uso da classe
pessoa1 = Pessoa(nome="ismael", idade=25, cpf=999-999-999-99)

# dados do pet
pet1 = pet(nome='toto',peso=4)

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f'CPF: {pessoa1.cpf}')

# Exibindo dados da pessoa
print('Exibindo dados')
print(f'Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\n')

# Exibindo dados dos pet
print('Dados do pet')
print(f'Nome: {pet1.nome}\nIdade: {pet1.idade}')
print(f'Peso: {pet1.peso}')