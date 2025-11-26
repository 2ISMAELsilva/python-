import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Funcionario:
    nome1: str
    data_admissao: int
    matricula: float
    endereco1: str
    
    def exibir_funcion(self):
        print(f'Nome: {self.nome} \n admissão: {self.data_admissao} \n Matriicula:{self.matricula} \n Endereço:{self.endereco1}')


    
@dataclass
class Cliente:
    nome2: str
    data_de_nascimento: float
    endereco2: str
    
    def exibir_dados(self):
        print(f'Nome: {self.nome2} \nNascimento: {self.data_de_nascimento} \n Endereço: {self.endereco2} \n')


FUNCIONARIOS = 3
CLIENTES = 3

for i in range (FUNCIONARIOS):
    funcionarios = Funcionario(
        nome1= input("Qual o seu nome? "),
        data_admissao= input('Qual a sua data de admissão? '),
        matricula= input('Qual a sua matricula? '),
        endereco1= input("Qual o seu Enderoço? ")
    )
    
for i in range(CLIENTES):
    clientes = Cliente(
        nome2= input('Qual seu nome? '),
        data_de_nascimento= input('Qual a sua data de nascimento? '),
        endereco2= input('Qual o seu endereço? ')
    )
    

vetor_funcionarios = []
vetor_clientes = []

vetor_funcionarios.append(Funcionario)
vetor_clientes.append(Cliente)


funcionarioo = "Dados_funcionario.csv"
with open(funcionarioo, "r") as arquivo_funcionarios:
    for pacientes in vetor_funcionarios:
        arquivo_funcionarios.write(f'{funcionarios.nome1} \n{funcionarios.data_admissao}\n {funcionarios.matricula} \n{funcionarios.endereco1}\n')
    print('Dados salvos com sucesso.')
        
        

client = "Dados_clientes.csv"
with open(client, "r") as arquivo_clientess:
    for pacientes in vetor_clientes:
        arquivo_clientess.write(f'{clientes.nome2} \n{clientes.data_de_nascimento}\n {clientes.endereco2}')
    print('Dados salvos com sucesso.')
        