import math
from functools import *
from VectorSpace import VectorSpace


class Vector(VectorSpace):

    # TODO: validate that all components are of int/float type
    def __init__(self, *components):
        self._components = list(components)

    # Multiplies a Vector by a Scalar.
    def __mul__(self, other):
        if self.is_scalar_not_correct_type(other):
            raise TypeError("The multiplication operator may only be used for Scalar factors.")

        return Vector(*[other * component for component in self._components])

    # See <__mul__>
    def __rmul__(self, other):
        return self * other

    # Divides a Vector by a Scalar.
    def __div__(self, other):
        if self.is_scalar_not_correct_type(other):
            raise TypeError("Can only divide by integers or floats.")

        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return Vector(*[component / other for component in self._components])

    # TODO: make this use __div__
    def __truediv__(self, other):
        if self.is_scalar_not_correct_type(other):
            raise TypeError("Can only divide by integers or floats.")

        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return Vector(*[component / other for component in self._components])

    # Prints the Vector components.
    def __str__(self):
        return "(" + ", ".join(str(component) for component in self._components) + ")"

    # Calculates the Dot product between this Vector and the other.
    def dot(self, other):
        if type(other) != Vector:
            raise TypeError("Dot product may only be calculated between two Vectors.")

        if self.is_not_same_length(other):
            raise IndexError("Vectors must be of the same dimension.")

        componentList = [selfVal * otherVal for selfVal, otherVal in zip(self._components, other._components)]

        return reduce(lambda x, y: x + y, componentList)

    # Calculates the Cross product between this Vector and the other.
    def cross(self, other):
        if type(other) != Vector:
            raise TypeError("Cross product may only be calculated between two Vectors.")

        if self.is_not_same_length(other):
            raise IndexError("Vectors must be of the same dimension.")

        # TODO: consider expanding this to 7 dimensions
        if len(self._components) != 3:
            raise ArithmeticError("Cross product may only be calculated in 3 dimensions.")

        return Vector(
            (self._components[1] * other._components[2] - self._components[2] * other._components[1]),
            -(self._components[0] * other._components[2] - self._components[2] * other._components[0]),
            (self._components[0] * other._components[1] - self._components[1] * other._components[0]))

    # Calculates the angle between this Vector and the other.
    # Result is in Radians by default - use the 'use_degrees' parameter to
    def angle_between(self, other, use_degrees=False):
        result = math.acos(self.dot(other) / (self.norm() * other.norm()))
        return math.degrees(result) if use_degrees else result

    # Determines whether this Vector is orthogonal (perpendicular) to the other.
    def is_orthogonal(self, other):
        return self.dot(other) == 0

    # Determines whether this Vector is parallel to the other.
    def is_parallel(self, other):
        return self.dot(other) == 1

    # Determines whether this Vector is antiparallel to the other.
    def is_antiparallel(self, other):
        return self.dot(other) == -1

    def is_same_length(self, other):
        return len(self._components) == len(other._components)

    def is_not_same_length(self, other):
        return not self.is_same_length(other)

    def is_scalar_correct_type(self, scalar):
        return type(scalar) == int or type(scalar) == float

    def is_scalar_not_correct_type(self, scalar):
        return not self.is_scalar_correct_type(scalar)