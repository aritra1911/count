"""Houses the Count class."""


class Count:
    """Count in any base."""

    def __init__(self, base=10):
        """Initialize counter with base."""
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
        """Increment by value."""
        if value == 0:
            return self.stigid[::-1]

        if len(self.stigid) == index:
            self.stigid.append(0)  # Code below takes care of the actual value

        incr_value = self.stigid[index] + value
        self.stigid[index] = incr_value % self.base
        return self.increment_by(incr_value // self.base, index+1)

    # TODO, Remove this as we got increment_by()
    def count(self):
        """
        Adds 1 (arithmetically) to existing
        list of digits and returns the list
        """
        def increment(index=0):
            limit = self.base - 1
            if len(self.stigid) == index:
                self.stigid = [0]*index
                self.stigid.append(1)
            elif self.stigid[index] < limit:
                self.stigid = [0]*index + self.stigid[index:]
                self.stigid[index] += 1
            elif self.stigid[index] == limit:
                increment(index + 1)

        increment()
        return self.stigid[::-1]  # invert and return

    def get_digits(self):
        """Return existing list of digits."""
        return self.stigid[::-1]

    def reset(self):
        """Reset count list to 0."""
        self.stigid = list()
