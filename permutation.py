from count import Count
from order import Order

import numpy as np


class Permutation(Order):
    def refresh(self):
        length = len(self.word)
        self.size = np.math.factorial(length) * length

    def generate_words(self):
        def is_distinct(digits):
            return not len(digits) > len(set(digits))

        c = Count(len(self.word))
        c.feed_zeroes(len(self.word))
        digits = c.get_digits()
        i = 0
        while i < np.math.factorial(len(self.word)):
            if is_distinct(digits):
                self.words.append([self.word[k] for k in digits])
                i += 1
            digits = c.increment_by(1)
        return self.words
