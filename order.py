class Order:
    def __init__(self, word = ''):
        self.word = list(word)
        self.words = list()
        self.size = 0
        self.refresh()

    def __len__(self):
        return self.size

    def set_word(self, word):
        self.word = list(word)

    def get_word(self):
        return str(self.word)

    def sort_word(self, desc = False):
        pass # apply your favorite sorting algorithm to sort self.word list

    def refresh(self):
        pass # Implemented in subclasses

    def generate_words(self):
        pass # Implemented in subclasses
