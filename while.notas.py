# import os 
# os.system('cls')

# calculo_media = 0 

# while True:
#     nota = float(input('DIGITE A SUA NOTA:'))
    
#     media = calculo_media + nota

#     mais_notas = input('DESEJAR POR MAIS UMA NOTA? \nUse (s ou n)')

#     if mais_notas == "n":
#         break

# print('==RESULTADO==')
# print(f'A media das notas são: {media}')

import os 
os.system('cls')


# Inicializando variáveis
soma = 0
contador = 0

while True:
    # Solicita uma nota do usuário
    nota = float(input("Digite uma nota: "))
    soma += nota
    contador += 1

    # Pergunta se deseja inserir mais uma nota
    resposta = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()

    if resposta == "N":
        break

# Calcula a média
if contador > 0:
    media = soma / contador
    print(f"Média das {contador} notas e: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
