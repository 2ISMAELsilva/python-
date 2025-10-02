import os 
os.system('cls')

# criando vetor
vetor_de_notas = []
QUANTIDADE = 3
print('Solicitando notas')
for i in range(QUANTIDADE):
    nota = float(input('digite uma nota: '))
    # incerindo uma nota na vetor de notas
    vetor_de_notas.append(nota)
    
print('\nMostrando todas as notas. ')
for i in range(QUANTIDADE):
    # O valor da variavel i começa com 0 
    # O valor de i no vetor faz mostrar o indice do vetor
    print(f'Nota: {vetor_de_notas[i]}') 
    