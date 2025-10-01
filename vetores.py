# vetores 

import os 
os.system('cls')

soma  = 0

# Colocando notas
for i in range(3):
    nota = int(input(f'Digite a {i+1} nota: '))
    soma += nota  
# mostrar nota
print(f'Nota: {nota}')
print(f'Nota: {soma}')
print('FIM')
