import os
os.system('cls')

# Lendo 6 numeros e informando quais são pares e quais são impares

# criando o vetor
lista_numeros = []

pares = 0
impares = 0

QUANTIDADE = 6

print("Solicitando 6 numeros e imformando os pares e impares")
for i in range(QUANTIDADE):
    numero = float(input(F'Digite {i+1} numero: '))
    lista_numeros.append(numero)   
    
    if numero % 2 == 0:
        pares += 1 
    else:
        impares += 1
        
print('imformando os numeros')
for i in range(QUANTIDADE):
    print(f'{i+1} numero informado: {lista_numeros[i]:.0f}')
    
print(f'Quantidades de pares: {pares}')
print(f'Quantidade de impares: {impares}')
 