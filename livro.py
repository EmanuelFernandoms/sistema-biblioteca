class Livro:
    def __init__(self, nome, autor,classificacao_indicativa, data_lanc, generos):
        self.nome = nome
        self.autor = autor
        self.classificacao_indicativa = classificacao_indicativa
        self.data_lanc = data_lanc
        self.generos = generos
        self.estaCom = 'biblioteca'