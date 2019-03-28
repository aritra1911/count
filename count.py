class Count:
    def __init__(self, base=10):
        self.set_base(base)
        self.stigid = list()  # Stores as OTH...
        self.sign = False

    def is_signed(self):
        return self.sign

    def set_base(self, base):
        """WARNING: Resets counter list."""
        self.base = base if base > 1 else 10
        self.reset()

    def feed_zeroes(self, zeroes):
        """Reset and load number of zeroes into counting list."""
        self.stigid = [0] * zeroes

    def set_number(self, digits):
        # TODO: Needs checking
        self.stigid = digits[::-1]

    def increment_by(self, value, index=0):
        if value == 0:
            return self.stigid[::-1]

        if len(self.stigid) == index:
            self.stigid.append(0)  # Code below takes care of the actual value

        incr_value = self.stigid[index] + value
        self.stigid[index] = incr_value % self.base
        return self.increment_by(incr_value // self.base, index+1)

    def decrement_by(self, value, index=0):
        decr_value = value % self.base
        self.stigid[index] -= decr_value
        has_borrowed = 0

        if self.stigid[index] < 0:
            self.stigid[index] += self.base
            has_borrowed = 1

        if index == len(self.stigid) - 1:
            while self.stigid and not self.stigid[-1]:
                self.stigid.pop()
            return self.stigid[::-1]

        next_sub = (value // self.base) + has_borrowed
        return self.decrement_by(next_sub, index + 1)


    def get_digits(self):
        return self.stigid[::-1]

    def reset(self):
        """Reset count list to 0."""
        self.stigid = list()
