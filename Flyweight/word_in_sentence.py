"""
Flyweight Coding Exercise

You are given a class called Sentence , which takes a string such as 'hello world'. You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a particular word in the sentence.

Typical use would be something like:

    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)  # writes "hello WORLD"

"""


class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(' ')
        self.tokens = {}

    def __getitem__(self, item):
        wt = self.WordToken()
        self.tokens[item] = wt
        return self.tokens[item]

    class WordToken:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __str__(self):
        result = []
        for i in range(len(self.words)):
            w = self.words[i]
            if i in self.tokens and self.tokens[i].capitalize:
                w = w.upper()
            result.append(w)
        return ' '.join(result)


sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)