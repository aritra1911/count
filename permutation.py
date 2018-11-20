from count import Count
from order import Order

class Permutation(Order):
    def fact(self, n):
            return 1 if n <= 1 else n*self.fact(n - 1)

    def refresh(self):
        length = len(self.word)
        self.size = self.fact(length) * length

    def generate_words(self):
        def is_distinct(digits):
            if len(digits) > len(set(digits)):
                return False
            return True

        c = Count(len(self.word))
        c.feed_zeroes(len(self.word))
        digits = c.get_digits()
        i = 0
        while i < self.fact(len(self.word)):
            if is_distinct(digits):
                self.words.append([self.word[k] for k in digits])
                i += 1
            digits = c.count()
        return self.words
