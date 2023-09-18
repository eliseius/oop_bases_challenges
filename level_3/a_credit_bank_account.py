"""
У нас есть класс кредитного банковского аккаунта со свойсвами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance
    
    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    bob = BankAccount(owner_full_name='Robert Nesta Marley', balance=250000.35)
    bob.increase_balance(amount=6990)
    bob.decrease_balance(amount=249900.1)

    ziggy = CreditAccount(owner_full_name='David Nesta Marley', balance=400.12)
    print(ziggy.is_eligible_for_credit())
    ziggy.increase_balance(amount=699)
    print(ziggy.is_eligible_for_credit())
    ziggy.decrease_balance(amount=200.1)
    print(ziggy.is_eligible_for_credit())

