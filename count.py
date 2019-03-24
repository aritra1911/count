class Count:
    def __init__(self, base=10):
        self.base = base if base > 1 else 10
        self.stigid = list()  # Stores as OTH...

    def set_base(self, base):
        """WARNING: Resets counter list."""
        self.base = base if base > 1 else 10
        self.reset()

    def feed_zeroes(self, zeroes):
        """Reset and load number of zeroes into counting list."""
        self.stigid = [0] * zeroes

    def increment_by(self, value, index=0):
        if value == 0:
            return self.stigid[::-1]

        if len(self.stigid) == index:
            self.stigid.append(0)  # Code below takes care of the actual value

        incr_value = self.stigid[index] + value
        self.stigid[index] = incr_value % self.base
        return self.increment_by(incr_value // self.base, index+1)

    def get_digits(self):
        return self.stigid[::-1]

    def reset(self):
        """Reset count list to 0."""
        self.stigid = list()
