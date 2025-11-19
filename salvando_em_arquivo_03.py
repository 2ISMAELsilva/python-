import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pacientes:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: int
    
    def exibir_dados(self):
        print(f'Nome: {self.nome} \n idade: {self.idade} \n Peso:{self.peso} \n Altura:{self.altura} \n CPF:{self.cpf}')

vetor_de_participantes = []
QUANTIDADE_PARTICIPANTES = 2 

for i in range(QUANTIDADE_PARTICIPANTES):
    pacientes = Pacientes(
        nome= input('Digite seu nome: '),
        idade= int(input('Digite sua idade:')),
        peso= float(input('Digite seu peso:')),
        altura= float(input('Digite a sua Altura: ')),
        cpf=  int(input('Digite o seu CPF: '))
    )
    vetor_de_participantes.append(pacientes)
    print() #pular uma linha

nome_do_arquivo = "Dados_pacientes.csv"
with open(nome_do_arquivo, "w") as arquivo_pacientes:
    for pacientes in vetor_de_participantes:
        arquivo_pacientes.write(f'{pacientes.nome} \n{pacientes.idade}\n {pacientes.peso} \n{pacientes.altura} \n {pacientes.cpf} \n')
    print('Dados salvos com sucesso.')
        
# print('\n Exibindo liasta de pacientes')
# for pacientes in vetor_de_participantes:
#     pacientes.exibir_dados()

print('\n Exibindo todos os pacientes')
try:
    with open(nome_do_arquivo,"r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print('O arquivo não foi encontrado. ')
    
 