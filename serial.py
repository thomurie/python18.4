"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    [start] = initial value
    
    [generate] = increase value of start by 1

    [restart] = return the augmented intial value to to the initial value
    
    """
    
    def __init__(self, start):
        self.start = start
        self.original = start

    def generate(self):
        self.start+=1
        return self.start
        
    def reset(self):
        self.start = self.original


serial = SerialGenerator(start=100)

print(serial.generate(),serial.generate(),serial.reset(), serial.generate(),serial.generate())
