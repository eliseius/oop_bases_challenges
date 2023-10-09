"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса Employee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self):
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float):
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, amount: float):
        self.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, amount: float):
        self.salary -= amount


class Developer(SuperAdminMixin, Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float, language: str):
        super().__init__(name, surname, age, salary)
        self.language = language
    
    def get_info(self):
        info = super().get_info()
        return f'{info}, programming language {self.language}'


if __name__ == '__main__':
    stas = Developer(name='Stas', surname='Eliseev', age=37, salary=120000.00, language='Python')
    stas.increase_salary(amount=25000)
    print(stas.get_info())
    stas.decrease_salary(amount=15000)
    print(stas.get_info())

