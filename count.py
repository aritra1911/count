class Count:
    def __init__(self, base=10):
        self.base = base if base > 1 else 10
        self.stigid = list()  # Stores as OTH...
        self.sign = False

    def is_signed():
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
        # TODO: Truncate meaningless zeroes at the start
        #       Also, think about refactoring entirely

        if value == 0:
            return self.stigid[::-1]

        place_value = self.stigid[index]
        decr_value = value % self.base

        if place_value < decr_value:
            i = 1
            while (index + i) < len(self.stigid):
                if self.stigid[index+i] > 0:
                    self.stigid[index] = place_value + self.base
                    self.stigid[index + i] -= 1
                    # if index + i+1 == len(self.stigid) and \
                    # self.stigid[index + i] == 0:
                    #     self.stigid = self.stigid[1:]
                    break
                elif self.stigid[index + i + 1] > 0:
                    self.stigid[index + i] = self.base - 1
                i += 1

        self.stigid[index] -= decr_value
        return self.decrement_by(value // self.base, index+1)

    def get_digits(self):
        return self.stigid[::-1]

    def reset(self):
        """Reset count list to 0."""
        self.stigid = list()
