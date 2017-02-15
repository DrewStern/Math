import math
from Vector import Vector
from VectorSpace import VectorSpace

# TODO: this will probably be phased out in favor of a general Multivector class -
# don't want to create classes which enumerate the number of Vector parameters that it takes
# that is, we don't want to bother creating Trivector, Quadvector, etc classes
# all of the necessary forms should be derived from the dimension of the underlying VectorSpace
class Bivector(VectorSpace):

    def __init__(self, first, second):
        if type(first) != Vector and type(second) != Vector:
            raise TypeError("Bivectors can only be constructed from Vectors")

        self.e1 = first
        self.e2 = second

    # Area of a Bivector is defined to be |q||p|*sin(angle_between(q, p)).
    def area(self):
        return self.e1.norm() * self.e2.norm() * math.sin(self.e1.dot(self.e2))

    # not real implementation
    def orientation(self):
        return self.e1 - self.e2 > 0

    # Dual of a Bivector is equivalent to the cross product of the two underlying Vectors.
    # TODO: review... might be missing a factor of i, in which case this becomes Complex(0,1)*(e1 cross e2)
    def dual(self):
        return self.e1*self.e2
