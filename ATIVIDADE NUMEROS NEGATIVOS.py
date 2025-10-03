import os 
os.system('cls')

valores = []
# valores_negativos = []
QUANTIDADE = 5 
for i in range(QUANTIDADE):
    numeros = float(input(f'Digite o {i+1} numero: '))
    if numeros < 0:
        valores.append(0)
    else:
        valores.append(numeros)
        
        
# print('Exibir numeros')
# for i in range(QUANTIDADE):
#     print(f'{i+1} numero: {valores[i]:.0f}')
    
    
    
print('Exibir numeros')
for i in enumerate(QUANTIDADE, start=1):
    print(f'{i+1} numero: {valores[i]:.0f}')
    