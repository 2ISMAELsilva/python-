import os 
os.system('cls')

# vetores

numeros_positivos = []
numeros_negativos = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numero = float(input(f'Digite o {i+1} numero: '))
    if numero < 0:
        numeros_negativos.append(numero)
    else:
        numeros_positivos.append(numero)
        
        
print(f'Numeros negativos: {len(numeros_negativos)}')
print(f'Soma dos numeros positivos: {sum(numeros_positivos):.0f}')
 