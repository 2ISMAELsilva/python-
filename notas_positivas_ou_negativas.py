
import os 
os.system('cls')


soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número inteiro positivo (ou negativo para sair): "))
    
    if numero < 0:  # condição de parada
        break
    
    soma += numero
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média aritmética é: {media:.2f}")
else:
    print("Nenhum número positivo foi informado.")
