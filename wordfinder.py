import random

class WordFinder:
    def __init__(self, path):
        self.path = path
        self.words = self.read_words()
        print(f"{len(self.words)} words read")

    def read_words(self):
        with open(self.path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    def read_words(self):
        with open(self.path, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        return words
