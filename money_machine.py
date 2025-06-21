

"""Módulo para gerenciar o processamento de dinheiro e transações."""

class MoneyMachine:
    """Gerencia o processamento de dinheiro, incluindo recebimento de moedas e cálculo de troco.

    Attributes:
        CURRENCY (str): O símbolo da moeda.
        COIN_VALUES (dict): Um dicionário mapeando nomes de moedas para seus valores.
        profit (float): O lucro acumulado pela máquina.
    """
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        """Inicializa a MoneyMachine com lucro zero."""
        self.profit = 0

    def report(self) -> None:
        """Imprime um relatório do lucro atual da máquina."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self) -> float:
        """Solicita ao usuário a inserção de moedas e calcula o total recebido.

        Returns:
            O valor total de dinheiro inserido pelo usuário.
        """
        print("Por favor, insira as moedas.")
        total = 0
        for coin in self.COIN_VALUES:
            try:
                total += int(input(f"Quantos {coin}? ")) * self.COIN_VALUES[coin]
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
        return round(total, 2)

    def make_payment(self, cost: float) -> bool:
        """Processa um pagamento, verifica se o dinheiro é suficiente e calcula o troco.

        Args:
            cost: O custo do item a ser pago.

        Returns:
            True se a transação for bem-sucedida, False caso contrário.
        """
        money_received = self.process_coins()
        if money_received >= cost:
            change = round(money_received - cost, 2)
            if change > 0:
                print(f"Aqui está {self.CURRENCY}{change} de troco.")
            self.profit += cost
            return True
        else:
            print("Desculpe, não há dinheiro suficiente. Dinheiro reembolsado.")
            return False


