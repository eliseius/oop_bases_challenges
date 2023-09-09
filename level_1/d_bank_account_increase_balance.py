"""
У нас есть класс банковского аккаунта со свойсвами: полное имя владельца и баланс, но не релизован
метод, который увеливает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечтайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income
        return self.balance


if __name__ == '__main__':
    account_instance = BankAccount(
        owner_full_name='Иванов Пётр',
        balance=145.2,
    )
    print(f'Баланс {account_instance.balance}')
    new_balance = round(account_instance.increase_balance(15.1),1)
    print(f'Новый баланс {new_balance}')