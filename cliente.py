class Cliente:
    def __init__(self, nome, numero, idade):
        self.nome = nome
        self.numero = numero
        self.idade = idade

    def pedir_livro(self, livro):
        if livro.classificacao_indicativa > self.idade:
            print('''
pedido cancelado pois classificação indicativa é maior que o permitido
            ''')
        elif livro.estaCom != 'biblioteca':
            print(f'''
o livro não se encontra na biblioteca
            ''')
        else:
            print(f'''
{self.nome} pediu o livro "{livro.nome}"          
            ''')

    def devolver_livro (self, livro):
        print(f'''
{self.nome} devolveu o livro "{livro.nome}"
        ''')
        livro.estaCom = 'biblioteca'