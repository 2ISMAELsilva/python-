# vetores
# notas de alunos


import os 
os.system('cls')

lista_notas = []


for i in range(4):
    nota = int(input(f'Digite a {i+1} nota: '))
    lista_notas.append(nota)
    
media = sum(lista_notas) / len(lista_notas)
    
        
for i in range(4):
    print(f'Nota: {i+4}: {lista_notas[i]}')

print(f'media: {media:2.1f}')
if media >=7:
    print('Aprovado')
elif media >=5:
    print('Recuperação')
else:
    print('Reprovado')
        
