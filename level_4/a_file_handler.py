"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json

from pathlib import Path


class FileHandler:
    def __init__(self, filename):
        self.filename = Path(Path.cwd(), 'data', filename)

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as jsonfile:
            file_load = json.load(jsonfile)
            return file_load


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as csvfile:
            file_reader = csv.DictReader(csvfile)
            users_data = [row for row in file_reader]
            return users_data


if __name__ == '__main__':
    users_info = FileHandler(filename='text.txt')
    print(users_info.read())

    recipes = JSONHandler(filename='recipes.json')
    print(json.dumps(recipes.read(), indent=4))

    users_info = CSVHandler(filename='user_info.csv')
    print(users_info.read())

