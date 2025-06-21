
"""Módulo que define o menu de bebidas e seus ingredientes/custos."""

class MenuItem:
    """Representa um item do menu da máquina de café.

    Attributes:
        name (str): O nome da bebida.
        water (int): A quantidade de água necessária (em ml).
        milk (int): A quantidade de leite necessária (em ml).
        coffee (int): A quantidade de café necessária (em gramas).
        cost (float): O custo da bebida (em USD).
    """
    def __init__(self, name: str, water: int, milk: int, coffee: int, cost: float):
        """Inicializa um MenuItem.

        Args:
            name: O nome da bebida.
            water: A quantidade de água necessária.
            milk: A quantidade de leite necessária.
            coffee: A quantidade de café necessária.
            cost: O custo da bebida.
        """
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


class Menu:
    """Gerencia os itens disponíveis no menu da máquina de café."""
    def __init__(self):
        """Inicializa o Menu com os itens de bebida predefinidos."""
        self.menu = [
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
        ]

    def get_items(self) -> str:
        """Retorna uma string com todos os nomes dos itens do menu, separados por barra.

        Returns:
            Uma string formatada com os nomes dos itens.
        """
        options = []
        for item in self.menu:
            options.append(item.name)
        return "/".join(options)

    def find_drink(self, order_name: str) -> MenuItem | None:
        """Encontra um item do menu pelo nome.

        Args:
            order_name: O nome da bebida a ser encontrada.

        Returns:
            O objeto MenuItem se encontrado, caso contrário, None.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Desculpe, esse item não está disponível.")
        return None


