class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return '☐' if self._ativo else '☒'


restaurante_praca = Restaurante('Praça', 'Comida Caseira')
restaurante_praca._ativo = True
restaurante_doce_sabor = Restaurante('Doce Sabor', 'Doces e Salgados')

Restaurante.listar_restaurantes()

