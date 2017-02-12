import math
from Vector import Vector
from VectorSpace import VectorSpace

class Bivector(VectorSpace):
    def __init__(self, first, second):
        if type(first) != Vector and type(second) != Vector:
            raise TypeError("Bivectors can only be constructed from Vectors")

        self.e1 = first
        self.e2 = second

    # not real implementation!
    def area(self):
        return self.e1.norm() * self.e2.norm() * math.sin(self.e1.dot(self.e2))

    # not real implementation
    def orientation(self):
        return self.e1 - self.e2 > 0

    # not real implementation
    def dual(self):
        pass
