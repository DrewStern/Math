import math
from Vector import Vector
from VectorSpace import VectorSpace

# A quaternion is a non-commutative element which can be denoted as
# a*1 + b*i + c*j + d*k for a, b, c, d in the Real numbers
# 1, i, j, k are the standard basis elements of the space
# the space is denoted as H (for Hamilton)
class Quaternion(VectorSpace):

    #def __init__(self, *components):
    #    self._components = list(components)
    def __init__(self, h = 0.0, i = 0.0, j = 0.0, k = 0.0):
        self._h = h
        self._i = i
        self._j = j
        self._k = k

    # multiplies a Quaternion by either another Quaternion or an integer/float
    # note that because H is noncommutative, q*p != p*q
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            #return Quaternion(*[other*component for component in self._components])
            return Quaternion(other*self._h, other*self._i, other*self._j, other*self._k)
        elif type(other) == Quaternion:
            return Quaternion(
                (self._h * other._h) - (self._i * other._i) - (self._j * other._j) - (self._k * other._k),
                (self._h * other._i) + (self._i * other._h) + (self._j * other._k) - (self._k * other._j),
                (self._h * other._j) - (self._i * other._k) + (self._j * other._h) + (self._k * other._i),
                (self._h * other._k) + (self._i * other._j) - (self._j * other._i) + (self._k * other._h))

            #scalarPart = self.scalar_part()*other.scalar_part() - self.vector_part().dot(other.vector_part())
            #vectorPart1 = self.scalar_part()*other.vector_part()
            #vectorPart2 = self.vector_part()*other.scalar_part()
            #vectorPart3 = self.vector_part()*other.vector_part()
            #totalVectorPart = vectorPart1+vectorPart2+vectorPart3
            return Quaternion(scalarPart, totalVectorPart)

    def __rmul__(self, other):
        return self*other

    # divides a Quaternion by an integer
    # TODO: ensure that 'other' is a valid type
    def __div__(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        #return Quaternion(*[component/other for component in self._components])
        return Quaternion(self._h/other, self._i/other, self._j/other, self._k/other)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        #return Quaternion(*[component/other for component in self._components])
        return Quaternion(self._h/other, self._i/other, self._j/other, self._k/other)

    # raises a Quaternion to an integer power
    def __pow__(self, power):
        if type(power) != int:
            raise TypeError("Raising a Quaternion to a non-integer power is not allowed.")
        
        if power == 0:
            return Quaternion(1, 0, 0, 0)
        if power > 0:
            return self*(self**(power-1))
        # TODO
        if power < 0:
            pass

    # prints the Quaternion components
    def __str__(self):
        #return "(" + ", ".join(str(component) for component in self._components) + ")"
        return "({0}, {1}, {2}, {3})".format(self._h, self._i, self._j, self._k)

    # creates a conjugate of the Quaternion
    def conjugate(self):
        return Quaternion(self.scalar_part(), -self.vector_part())

    # creates a reciprical of the Quaternion such that q*reciprocal(q) == 1
    def reciprocal(self):
        length = self.norm()**2
        if length == 0:
            raise ZeroDivisionError("Unable to divide by zero.")
        return self.conjugate() / length

    # TODO: need a test for this
    def exp(self):
        coefficient = math.e**self.h
        evenPart = Quaternion(math.cos(self.norm()), 0, 0, 0)
        oddPart = self.normalize()*math.sin(self.norm())

        print("\n", "coefficient ==", coefficient)
        print("\n", "evenPart == ", evenPart)
        print("\n", "oddPart == ", oddPart)
        print("\n", "e^q == ", coefficient*(evenPart + oddPart))
        
        return coefficient*(evenPart + oddPart)

    def scalar_part(self):
        #return self._components[0]
        return self._h
    
    def vector_part(self):
        #return Vector(self._components[1], self._components[2], self._components[3])
        return Vector(self._i, self._j, self._k)

    def is_scalar(self):
        #return self._components[1] == 0 and self._components[2] == 0 and self._components[3] == 0
        return self._i == 0 and self._j == 0 and self._k == 0
