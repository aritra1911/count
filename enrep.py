from count import Count

FIXED_LENGTH = False
UPTO_LENGTH  = True

class Enrep:
    def __init__(self, word = '', length = None, mode = UPTO_LENGTH):
        self.word = list(word)
        self.length = length if length is not None else len(self.word)
        self.mode = mode
        self.refresh()

    def __len__(self):
        return self.size

    def set_word(self, word):
        self.word = list(word)

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

    def get_size(self):
        return self.size

    def generate_words(self):
        self.words = list()
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
