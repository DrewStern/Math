import math
from Vector import Vector
from VectorSpace import VectorSpace

class Bivector(VectorSpace):
    def __init__(self, first, second):
        if type(first) != Vector or type(second) != Vector:
            raise TypeError("Bivectors can only be constructed from Vectors")

        self.e1 = first
        self.e2 = second

    # not real implementation!
    def get_area(self):
        return self.e1 * self.e2 * math.sin(self.e1 - self.e2)

    # not real implementation
    def get_orientation(self):
        return self.e1 - self.e2 > 0