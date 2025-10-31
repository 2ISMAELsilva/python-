import os 
from dataclasses import dataclass
os.system('cls')

@dataclass
class Autor:
    nome: str
    biografia: str
    
@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor
    
    def exibir_detalhes(self):
        print(f'\nTitulo: {self.titulo}')
        print(f'Ano: {self.ano} ')
        print(f'Autor: {self.autor.nome} ')
        print(f"Biografia do autor: {self.autor.biografia}")


dados_clientes = Livro(titulo=input('Informe o Titulo: '),
                             ano=input('Informe o Ano: '),
                             autor=Autor(nome=input("Nome do autor: "),
                                         biografia=input("Digite a biografia: ")))    

os.system('cls')
print('===== MOSTRANDO INFORMAÇÕES =====')
dados_clientes.exibir_detalhes()