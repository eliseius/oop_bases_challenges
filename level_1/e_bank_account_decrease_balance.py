"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income
        return round(self.balance,1)

    def decrease_balance(self, income: float):
        self.balance -= income
        if self.balance < 0:
            raise ValueError
        return round(self.balance, 1)


if __name__ == '__main__':
    account_instance = BankAccount(
        owner_full_name='Петров Иван',
        balance=1949.9,
    )

    new_balance = account_instance.decrease_balance(999)
    print(f'Новый баланс до положительного {new_balance}')
    new_balance = account_instance.decrease_balance(1999)
