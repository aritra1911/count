from count import Count
from order import Order

FIXED_LENGTH = False
UPTO_LENGTH  = True

class Enrep(Order):
    def __init__(self, word = '', length = None, mode = UPTO_LENGTH):
        length = int(length if length is not None else len(word))
        self.length = length
        self.set_mode(mode)
        super().__init__(word)

    def set_length():
        self.length = length if length is not None else len(self.word)

    def get_length():
        return self.length

    def set_mode(self, mode):
        self.mode = bool(mode)

    def refresh(self):
        # Calculate number of words that can be made
        self.size = 0
        if not (len(self.word) == 0 or self.length == 0):
            if self.mode == UPTO_LENGTH:
                for i in range(1, self.length + 1):
                    self.size += (len(self.word)**i) * i
            else:
                self.size = (len(self.word)**self.length) * self.length

    def generate_words(self):
        c = Count(len(self.word))
        if self.mode == UPTO_LENGTH:
            for i in range(1, self.length + 1):
                c.feed_zeroes(i)
                l = c.get_digits()
                for j in range(len(self.word)**i):
                    self.words.append([self.word[k] for k in l])
                    l = c.count()
        else:
            c.feed_zeroes(self.length)
            l = c.get_digits()
            for i in range(len(self.word)**self.length):
                self.words.append([self.word[k] for k in l])
                l = c.count()
        return self.words
