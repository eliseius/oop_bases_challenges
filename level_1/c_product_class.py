"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int, weight: int):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight


if __name__ == '__main__':
    product_instance = Product(
        name='Garland "You are art"',
        description='Бумажная текстовая гирлянда из матового дизайнерского картона плотностью 250г/м2 чёрного цвета',
        price=548,
        weight=50,
    )
    print(f'Информация о продукте: {product_instance.name}, {product_instance.description}, {product_instance.price}, {product_instance.weight}')