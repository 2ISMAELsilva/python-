lista_clientes = []

print('CREAT - Adicionar / Inserir')
nome = input('Digite o seu nome: ')
lista_clientes.append(nome)
print(f'O nome: {nome} Foi imserido com sucesso!!')

# READ
print('\nRead - ler')
print(lista_clientes)

# UPGRAD
print('\n Atualizar / Alterar')
nome_para_atualizar = input('Digite o novo nome: ')
if nome_para_atualizar in lista_clientes:
    novo_nome = {nome_para_atualizar}
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes[indice] = novo_nome
    print(f'O nome {nome_para_atualizar} foi atualizado! ')
else:
    print(f'O nome: {nome_para_atualizar} não foi encontrado')
    
# DELETE
print("\nDelete - Excluir / Remover")
nome_para_excluir = {nome}
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluído com sucesso!")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)

