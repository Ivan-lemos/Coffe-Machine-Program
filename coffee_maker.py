

"""Módulo para gerenciar os recursos e a preparação do café na máquina de café."""

class CoffeeMaker:
    """Gerencia os recursos (água, leite, café) e a preparação das bebidas.

    Attributes:
        resources (dict): Um dicionário que armazena as quantidades atuais de água, leite e café.
    """
    def __init__(self):
        """Inicializa o CoffeeMaker com os recursos iniciais."""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self) -> None:
        """Imprime um relatório dos recursos atuais disponíveis na máquina."""
        print(f"Water: {self.resources["water"]}ml")
        print(f"Milk: {self.resources["milk"]}ml")
        print(f"Coffee: {self.resources["coffee"]}g")

    def is_resource_sufficient(self, drink_ingredients: dict) -> bool:
        """Verifica se há recursos suficientes para fazer a bebida solicitada.

        Args:
            drink_ingredients: Um dicionário com os ingredientes necessários para a bebida.

        Returns:
            True se houver recursos suficientes, False caso contrário.
        """
        for item in drink_ingredients:
            if drink_ingredients[item] > self.resources.get(item, 0):
                print(f"Desculpe, não há {item} suficiente.")
                return False
        return True

    def make_coffee(self, drink_name: str, order_ingredients: dict) -> None:
        """Prepara a bebida e deduz os ingredientes dos recursos.

        Args:
            drink_name: O nome da bebida a ser preparada.
            order_ingredients: Um dicionário com os ingredientes necessários para a bebida.
        """
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Aqui está o seu {drink_name}. Aproveite!")


