"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знает о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


class PrintLoggerMixin():
    def log(self, message: str):
        print(message)


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self):
        self.price *= 1.2

    def get_info(self):
        base_info = super().get_info()
        text = f'{base_info} (Premium)'
        super().log(message=text)
        return text


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self):
        self.price /= 1.2

    def get_info(self):
        base_info = super().get_info()
        text = f'{base_info} (Discounted)'
        super().log(message=text)
        return text


if __name__ == '__main__':
    lemon = PremiumProduct(title='Лимон', price=2.45)
    lemon.increase_price()
    lemon.get_info()

    tomato = DiscountedProduct(title='Помидор', price=4.23)
    tomato.decrease_price()
    tomato.get_info()

