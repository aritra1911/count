class Count:
    def __init__(self, base = 10):
        self.base = base if base > 1 else 10
        self.stigid = list() # Stores as OTH...

    def set_base(self, base):
        """
        WARNING: Resets counter list
        """
        self.base = base if base > 1 else 10
        self.reset()

    def feed_zeroes(self, n):
        """
        Resets and loads n number of zeroes into counting list
        """
        self.stigid = [0] * n

    def count(self):
        """
        Adds 1 (arithmetically) to existing
        list of digits and returns the list
        """
        def increment(index = 0):
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
        return self.stigid[::-1] # invert and return

    def get_digits(self):
        """
        Returns existing list of digits
        """
        return self.stigid[::-1]

    def reset(self):
        """
        Resets counting list to 0
        """
        self.stigit = list()
