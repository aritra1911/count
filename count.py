class Count:
    def __init__(self, base = 10):
        self.base = base if base > 1 else 10
        self.digits = [0]
        self.stigid = list() # Stores as OTH...

    def count(self):
        """
        Adds 1 (arithmetically) to existing
        list of digits and returns the list
        """
        def increment(index = 0):
            limit = self.base - 1
            if len(self.stigid) == index:
                self.stigid = [0 for i in range(index)]
                self.stigid.append(1)
            elif self.stigid[index] < limit:
                self.stigid = [0 for i in range(index)] + self.stigid[index:]
                self.stigid[index] += 1
            elif self.stigid[index] == limit:
                increment(index + 1)

        increment()
        self.digits = self.stigid[::-1] # invert and store
        return self.get_digits()

    def get_digits(self):
        """
        Returns existing list of digits
        """
        return self.digits
