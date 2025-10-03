import os 
os.system('cls')

def saudacao(nome, idade, peso, altura):
    print(f'Ola, {nome}! Bem vindo(a)')
    print(f'Sua idade e: {idade}')
    print(f'Seu peso e: {peso}')
    print(f'Sua altura e: {altura}')
# solicitando dados
nome = input('DIGITE SEU NOME: ')
idade = int(input('DIGITE SUA IDADE: '))
peso = float(input('DIGITE SEU PESO: '))
altura = float(input('INFORME A SUA ALTURA: '))
# chamando a função
saudacao(nome,idade,peso, altura )
