import math

from src.Tools import Tools
from src.Vector import Vector
from src.VectorSpace import VectorSpace


# A Quaternion is an element which can be denoted as a*1 + b*i + c*j + d*k for a, b, c, d in the Real numbers.
# This space is denoted as H (for Hamilton), and has 1, i, j, k as its standard basis elements.

# Note that despite the fact that this inherits from VectorSpace, the Quaternions do not actually form a
# Vector Space, because any two elements of H are anti-commutative with one another. That is: q*p != p*q.
class Quaternion(VectorSpace):

    # Constructor for the Quaternion class.
    def __init__(self, h=0.0, i=0.0, j=0.0, k=0.0):
        self._h = h
        self._i = i
        self._j = j
        self._k = k

        # this only exists in order to leverage the inheritance from VectorSpace
        self._components = [self._h, self._i, self._j, self._k]

    # Multiplies a Quaternion by either another Quaternion or an integer/float,
    def __mul__(self, other):
        if Tools.is_numeric_type(other):
            return Quaternion(other * self._h, other * self._i, other * self._j, other * self._k)
        elif type(other) == Quaternion:
            return Quaternion(
                (self._h * other._h) - (self._i * other._i) - (self._j * other._j) - (self._k * other._k),
                (self._h * other._i) + (self._i * other._h) + (self._j * other._k) - (self._k * other._j),
                (self._h * other._j) - (self._i * other._k) + (self._j * other._h) + (self._k * other._i),
                (self._h * other._k) + (self._i * other._j) - (self._j * other._i) + (self._k * other._h))

    # The left-multiplication method __mul__ already handles the anti-commutativity.
    def __rmul__(self, other):
        return self * other

    # Divides a Quaternion by an integer.
    def __div__(self, other):
        if Tools.is_not_numeric_type(other):
            raise TypeError("Can only divide by integers or floats.")
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Quaternion(self._h / other, self._i / other, self._j / other, self._k / other)

    # TODO: make this leverage the existing __div__ method
    def __truediv__(self, other):
        return self.__div__(other)

    # Raises a Quaternion to an integer power.
    def __pow__(self, power):
        if type(power) != int:
            raise TypeError("Raising a Quaternion to a non-integer power is not allowed.")
        if power == 0:
            return Quaternion(1, 0, 0, 0)
        if power > 0:
            return self * (self ** (power - 1))
        # TODO
        if power < 0:
            pass

    # Prints the Quaternion components.
    def __str__(self):
        return "({0}, {1}, {2}, {3})".format(self._h, self._i, self._j, self._k)

    # Creates a conjugate of the Quaternion.
    def conjugate(self):
        return Quaternion(self._h, -self._i, -self._j, -self._k)

    # Creates a reciprocal of the Quaternion such that q*reciprocal(q) == 1
    def reciprocal(self):
        length = self.norm() ** 2
        if length == 0:
            raise ZeroDivisionError("Unable to divide by zero.")
        return self.conjugate() / length

    # TODO: need a test for this
    def exp(self):
        coefficient = math.e ** self.h
        evenPart = Quaternion(math.cos(self.norm()), 0, 0, 0)
        oddPart = self.normalize() * math.sin(self.norm())

        print("\n", "coefficient ==", coefficient)
        print("\n", "evenPart == ", evenPart)
        print("\n", "oddPart == ", oddPart)
        print("\n", "e^q == ", coefficient * (evenPart + oddPart))

        return coefficient * (evenPart + oddPart)

    # Returns the Scalar component of this Quaternion.
    def scalar_part(self):
        return self._h

    # Returns the Vector component of this Quaternion.
    def vector_part(self):
        return Vector(self._i, self._j, self._k)

    # Discerns whether the Vector component of this Quaternion is zero.
    def is_scalar(self):
        return self._i == 0 and self._j == 0 and self._k == 0

    # Discerns whether the Scalar component of this Quaternion is zero.
    def is_vector(self):
        return self._h == 0
