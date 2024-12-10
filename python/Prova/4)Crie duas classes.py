'''
4)Crie duas classes:
1 Autor, com os atributos:  Nome, nacionalidade e livros
2 Livro, com os atributos: titulo, ano e autor
Depois, escreva um programa que:Crie um autor e dois livros associados a ele.
Imprima o nome do autor e a lista dos seus livros.

'''

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} ({self.ano})"


class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def __str__(self):
        return self.nome


autor = Autor("J.K. Rowling", "Britânica")

livro1 = Livro("Harry Potter e a Pedra Filosofal", 1997, autor)
livro2 = Livro("Harry Potter e a Câmara Secreta", 1998, autor)

autor.adicionar_livro(livro1)
autor.adicionar_livro(livro2)

print(f"Autor: {autor}")
print("Livros:")
for livro in autor.livros:
    print(f"- {livro}")



