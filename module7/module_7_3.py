from pprint import pprint
from typing import Dict, Any


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                #print(f)
                for sym in [',', '.','=','!','?',':',';',' - ']:
                    info= info.replace(sym,' ')
                    all_words[name] = info.split()

            return all_words
    def find(self, word):
        self.word=word
        for self.word in self.get_all_words().items():
            #return self.get_all_words().find(self.word.lower())
            return self.word
                


           # count= self.get_all_words().
       # print(count)





finder2 = WordsFinder('file1.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
#(finder2.count('teXT'))
