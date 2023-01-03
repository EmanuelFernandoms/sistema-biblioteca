from biblioteca import Biblioteca
from cliente import Cliente
from livro import Livro

biblioteca1 = Biblioteca('biblioteca garopaba')

livro1 = Livro('harry potter','Rowling',16 , 1960, 'fantasia')
livro2 = Livro('percy jackson', 'Riordan',14 , 1980, 'suspense')
livro3 = Livro('senhor dos aneis','tolkien',18 , 1998,'aventura')

cliente1 = Cliente('roberto', '2190432103', 20)
cliente2 = Cliente('heitor', '89417249817', 16)
cliente3 = Cliente('arthur petry', '7816478126', 13)

biblioteca1.adicionar_livro(livro1)
biblioteca1.adicionar_livro(livro2)
biblioteca1.adicionar_livro(livro3)