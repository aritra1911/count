class Order:
    def __init__(self, word=''):
        self.word = list(word)
        self.words = list()
        self.size = 0
        self.refresh()

    def __len__(self):
        return self.size

    def set_word(self, word):
        self.word = list(word)

    def get_word(self):
        return ''.join(self.word)

    def sort_word(self, desc=False):
        def swappable(a, b):
            return a > b if desc else a < b

        # Bubble sort
        for j in range(len(self.word)):
            for i in range(j + 1, len(self.word)):
                if swappable(self.word[i], self.word[j]):
                    self.word[i], self.word[j] = self.word[j], self.word[i]

    def refresh(self):
        pass  # Implemented in subclasses

    def generate_words(self):
        pass  # Implemented in subclasses
