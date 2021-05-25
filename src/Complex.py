import math

from src.Tools import Tools
from src.VectorSpace import VectorSpace


class Complex(VectorSpace):

    # TODO: enforce len(components) == 2
    def __init__(self, *components):
        if len(components) != 2:
            raise IndexError("Complex numbers may only have 2 components.")
        self._components = list(components)

    # multiplies a Complex by either another Complex or an integer/float
    def __mul__(self, other):
        if Tools.is_numeric_type(other):
            return Complex(*[other * component for component in self._components])
        elif Tools.are_same_type(self, other):
            return Complex(self.real_part() * other.real_part() - self.imaginary_part() * other.imaginary_part(),
                           self.real_part() * other.imaginary_part() + self.imaginary_part() * other.real_part())

    def __rmul__(self, other):
        return self * other

    # divides a Complex by an integer
    # TODO: need to be able to divide by Complexes
    def __div__(self, other):
        if Tools.is_not_numeric_type(other):
            raise TypeError("Can only divide by integers or floats.")
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Complex(*[component / other for component in self._components])

    def __truediv__(self, other):
        return self.__div__(other)

    # raises a Complex to an integer power
    def __pow__(self, power):
        if type(power) != int:
            raise TypeError("Raising a Complex to a non-integer power is not allowed.")
        if power == 0:
            return Complex(1, 0)
        if power > 0:
            return self * (self ** (power - 1))
        # TODO: need a test for this case
        if power < 0:
            return self.reciprocal() * (self.reciprocal() ** (power - 1))

    # prints the Complex components
    def __str__(self):
        return "(" + ", ".join(str(component) for component in self._components) + ")"

    # creates a conjugate of the Complex
    def conjugate(self):
        return Complex(self.real_part(), -self.imaginary_part())

    # creates a reciprical of the Complex such that c*reciprocal(c) == 1
    def reciprocal(self):
        hypoteneuse = self.norm() ** 2
        if hypoteneuse == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.conjugate() / hypoteneuse

    # TODO: fix this
    def exp(self):
        coefficient = math.e ** self.r
        return

    def real_part(self):
        return self._components[0]

    def imaginary_part(self):
        return self._components[1]

    def is_real(self):
        return self.imaginary_part() == 0

    def is_imaginary(self):
        return self.real_part() == 0
