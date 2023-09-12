"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        total_words = len(self.text.split())
        return f'Total text length: {len(self.text)}, total number of words in the text: {total_words}'


if __name__ == '__main__':
    text = 'Бесплатный сервис Google позволяет мгновенно переводить слова, фразы и веб-страницы. Поддерживается более 100 языков.'
    text_structure = TextProcessor(text=text)
    print(text_structure.to_upper())
    print(text_structure.summarize())

    text = 'Google Переводчик (англ. Google Translate) — веб-служба компании Google, предназначенная для автоматического перевода части текста или веб-страницы на другой язык.'
    text_structure = AdvancedTextProcessor(text=text)
    print(text_structure.to_upper())
    print(text_structure.summarize())
