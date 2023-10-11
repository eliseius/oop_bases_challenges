"""
Мы используем константу EBAY_TITLE только в классе EbayProduct и хочется чтобы она жила в классе, а не где-то отдельно

Задания:
    1. Сделайте так, чтобы тайтл ебэя жил в классе
    2. Создайте экземпляр класса EbayProduct, вызовите у него метод get_product_info и убедитесь, что метод отдает
       то что вы ожидаете.
"""


class EbayProduct:
    EBAY_TITLE = 'eBay'

    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_product_info(self):
        
        return f'Product {self.title} with price {self.price} from {self.EBAY_TITLE} marketplace'


if __name__ == '__main__':
    table = EbayProduct(title='Стол круглый', price=15241.3)
    print(table.get_product_info())
