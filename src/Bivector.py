import math

from src.Tools import Tools
from src.VectorSpace import VectorSpace


# TODO: this will probably be phased out in favor of a general Multivector.py class -
# don't want to create classes which enumerate the number of Vector parameters that it takes
# that is, we don't want to bother creating Trivector, Quadvector, etc classes
# all of the necessary forms should be derived from the dimension of the underlying VectorSpace
class Bivector(VectorSpace):

    def __init__(self, first, second):
        if Tools.are_not_same_type(first, second):
            raise TypeError("Bivectors can only be constructed from Vectors")
        self._e1 = first
        self._e2 = second

    # Area of a Bivector is defined to be |q||p|*sin(angle_between(q, p)).
    def area(self):
        return self._e1.norm() * self._e2.norm() * math.sin(self._e1.angle_between(self._e2))

    # not real implementation
    def orientation(self):
        return self._e1 - self._e2 > 0

    # Dual of a Bivector is equivalent to the cross product of the two underlying Vectors.
    # TODO: review... might be missing a factor of i, in which case this becomes Complex(0,1)*(e1 cross e2)
    def dual(self):
        return self._e1.cross(self._e2)
