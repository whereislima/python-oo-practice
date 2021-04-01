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
    """
    def __init__(self, start=0):
        """ """
        self.start = start
        
    def __repr__(self):
        """Returns a string representation"""
        return f"start={self.start} next={self.next"
    
    def generate(self): 
        """Returns next serial number"""
        self.next += 1
        return self.next - 1 
        

    def reset(self):
        """Reset number to start"""

        self.next = self.start
        

