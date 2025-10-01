# vetores

lista_notas = []

for i in range(3):
    nota = int(input(f'Digite a {i+1} nota: '))
    lista_notas.append(nota)
    
 
    soma = sum(lista_notas) / len(lista_notas)
         
for i in range(3):
    print(f'Nota: {lista_notas[i]}')

print(f'Nota: {soma:2.2f}')
