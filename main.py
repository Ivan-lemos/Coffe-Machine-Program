from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    """Inicia e gerencia a operação da máquina de café.

    Esta função é o ponto de entrada principal para a máquina de café.
    Ela interage com o usuário, processa pedidos, verifica recursos,
    gerencia pagamentos e prepara bebidas.
    """
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True

    while is_on:
        options = menu.get_items()
        choice = input(f"O que você gostaria? ({options}): ").lower()

        if choice == "off":
            is_on = False
            print("Desligando a máquina de café.")
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink.ingredients):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink.name, drink.ingredients)


if __name__ == "__main__":
    coffee_machine()


