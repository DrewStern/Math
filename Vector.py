import math
from VectorSpace import VectorSpace
from itertools import *
from functools import *

class Vector(VectorSpace):

    def __init__(self, *components):
        self._components = list(components)

    # Multiplies two Vectors via the cross product or a Vector and an integer/float. The cross product is treated as
    # the default multiplication of Vectors simply because it returns an object of the same type as the inputs.
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(*[other*component for component in self._components])
        elif type(other) == Vector and len(self._components) == len(other._components) == 3:
            return Vector(
                (self._components[1]*other._components[2] - self._components[2]*other._components[1]),
                -(self._components[0]*other._components[2] - self._components[2]*other._components[0]),
                (self._components[0]*other._components[1] - self._components[1]*other._components[0]))

    def __rmul__(self, other):
        return self*other

    # divides a Vector by an integer
    # TODO: ensure that 'other' is a valid type
    def __div__(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return Vector(*[component/other for component in self._components])

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return Vector(*[component/other for component in self._components])

    # Prints the Vector components.
    def __str__(self):
        return "(" + ", ".join(str(component) for component in self._components) + ")"

    # the dot product is treated as a separate method rather than the default
    # multiplication because it produces a Scalar rather than a Vector
    def dot(self, other):
        if len(self._components) != len(other._components):
            raise IndexError("Vectors must be of the same length.")
        
        componentList = [selfVal*otherVal for selfVal, otherVal in zip(self._components, other._components)]
        return reduce(lambda x, y: x+y, componentList)

    # Determines whether this Vector is orthogonal (perpendicular) to the other Vector.
    def is_orthogonal(self, other):
        return self.dot(other) == 0

    # Determines whether this Vector is collinear (parallel) to the other Vector.
    def is_collinear(self, other):
        return self.dot(other) == 1 or self.dot(other) == -1
