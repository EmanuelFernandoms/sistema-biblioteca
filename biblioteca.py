class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def disponibilizar_pedido (self, livro, cliente):
        print(f'''
o livro "{livro.nome}" foi disponibilizado para {cliente.nome}
        ''')
        livro.estaCom = cliente.nome

    def rejeitar_pedido (self, livro, cliente):
        print(f'''
o livro "{livro.nome}" foi negado para {cliente.nome}
        ''')

    def localizar_livro (self, livro):
      print(f'''
o livro "{livro.nome}" está junto de {livro.estaCom}
      ''')

    def adicionar_livro (self, livro):
        self.livros.append (livro)

    def mostrar_acervo (self):
      for livro in self.livros:
        print(f'''
livro: {livro.nome}
esctrito por: {livro.autor} 
generos:{livro.generos}
''')