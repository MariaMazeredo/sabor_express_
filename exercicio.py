# Crie uma classe chamada Carro com um construtor que aceita os parâmetros modelo, cor e ano.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_1 = Carro("Fusca", "Branco", 1977)
carro_2 = Carro("Gol", "Preto", 2005)
carro_3 = Carro("Omega", "Prata", 1995)

# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
        
conta_1 = ContaBancaria("João Silva", 1500.00)
conta_2 = ContaBancaria("Maria Oliveira", 2500.50)
conta_3 = ContaBancaria("Carlos Souza", 320.75)

# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

livro_1 = Livro("O morro dos ventos uivantes", "Emily Brontë", 1847)
livro_2 = Livro("Moby dick", "Herman Melville", 1851)
livro_3 = Livro("O pequeno príncipe", "Antoine de Saint-Exupéry", 1943)

# Crie uma classe chamada Restaurante com um construtor que aceita os parâmetros nome e categoria. Inicie o atributo ativo como False por padrão.

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_1 = Restaurante("Sabor da Terra", "Comida Brasileira")
restaurante_2 = Restaurante("La Pasta", "Comida Italiana")

# Crie uma classe chamada Filme com um construtor que aceita os parâmetros titulo, diretor e ano_lancamento.

class Filme:
    def __init__(self, titulo, diretor, ano_lancamento):
        self.titulo = titulo
        self.diretor = diretor
        self.ano_lancamento = ano_lancamento

filme_1 = Filme("O Poderoso Chefão", "Francis Ford Coppola", 1972)
filme_2 = Filme("Forrest Gump", "Robert Zemeckis", 1994)
filme_3 = Filme("A Origem", "Christopher Nolan", 2010)

# Crie uma classe chamada Pessoa com um construtor que aceita os parâmetros nome, idade e cidade.

class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

pessoa_1 = Pessoa("Joelma, 30, Salvador")
pessoa_2 = Pessoa("Ximbinha, 60, Belém")
pessoa_3 = Pessoa("Faustão, 50, São Paulo")