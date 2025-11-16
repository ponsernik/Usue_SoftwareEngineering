class NegativeBalanceError(Exception):
    pass

# Первое использование
def check_balance(amount):
    if amount < 0:
        raise NegativeBalanceError("Баланс отрицательный")
    print("Баланс корректен")

# Второе использование
def transfer_money(from_acc, to_acc, amount):
    if amount < 0:
        raise NegativeBalanceError("Сумма перевода не может быть отрицательной")
    print(f"Перевод {amount} с {from_acc} на {to_acc}")

# Тестирование
try:
    check_balance(-100)
except NegativeBalanceError as e:
    print(f"Ошибка 1: {e}")

try:
    transfer_money("счет1", "счет2", -50)
except NegativeBalanceError as e:
    print(f"Ошибка 2: {e}")