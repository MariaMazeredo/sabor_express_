#arquivo principal do sistema

from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Comida Caseira')
restaurante_sargado = Restaurante('Salgadinho', 'Lanchonete')
restaurante_bella_pizza = Restaurante('Bella Pizza', 'Pizza')

restaurante_bella_pizza.alterar_status()    
restaurante_bella_pizza.receber_avaliacao('Ana', 5)
restaurante_bella_pizza.receber_avaliacao('Bruno', 4)
restaurante_bella_pizza.receber_avaliacao('Carla', 4)


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()