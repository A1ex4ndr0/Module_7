class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                _list = []
                for line in file:
                    line = line.lower()
                    for symb in line:
                        if symb in punc:
                            line = line.replace(symb, "")
                    words = line.split()
                    for j in words:
                        _list.append(j)
            all_words[i] = _list
        return all_words

    def find(self, word):
        _dict = {}
        for name, words in self.get_all_words().items():
            _dict[name] = [s.lower() for s in words].index(word.lower()) + 1
        return _dict

    def count(self, word):
        _dict = {}
        for name, words in self.get_all_words().items():
            _count = 0
            for i in words:
                if word.lower() == i.lower():
                    _count += 1
            _dict[name] = _count
        return _dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt')
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))