import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    text = f.read().lower()
                    for punc in punctuation_to_remove:
                        text = text.replace(punc, '')  # Убираем пунктуацию
                    words = text.split()  # Разбиваем на слова
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File {file_name} not found.")

        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Возвращаем индекс первого слова (с учётом 1-индексации)
            else:
                result[file_name] = -1  # Если слово не найдено, возвращаем -1

        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            result[file_name] = words.count(word)  # Считаем количество вхождений

        return result


# Пример использования:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))     # Позиция первого вхождения слова 'TEXT'
print(finder2.count('teXT'))    # Количество вхождений слова 'teXT'