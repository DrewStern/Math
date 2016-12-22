from abc import ABCMeta, abstractmethod
import copy
import math

class VectorSpace():
    __metaclass__ = ABCMeta

    # override the + operator for elements of the Vector Space
    @abstractmethod
    def __add__(self, other):
        if type(self) != type(other):
            return None
        if len(self._components) != len(other._components):
            raise IndexError("Vectors must be of the same length.")
        newObj = copy.copy(self)
        newObj._components = [selfVal + otherVal for (selfVal, otherVal) in zip(self._components, other._components)]
        return newObj

    @abstractmethod
    def __radd__(self, other):
        return self + other

    # override the - operator for elements of the Vector Space
    @abstractmethod
    def __sub__(self, other):
        if type(self) != type(other):
            return None
        if len(self._components) != len(other._components):
            raise IndexError("Vectors must be of the same length.")
        newObj = copy.copy(self)
        newObj._components = [selfVal - otherVal for (selfVal, otherVal) in zip(self._components, other._components)]
        return newObj

    @abstractmethod
    def __rsub__(self, other):
        return self - other

    # using the caller, derives a new element of the Vector Space with each component negated
    @abstractmethod
    def __neg__(self):
        newObj = copy.copy(self)
        newObj._components = [-component for component in self._components]
        return newObj

    # calculates the length of the caller
    @abstractmethod
    def norm(self):
        newObj = copy.copy(self)
        sumOfSquares = 0.0
        for component in self._components:
            sumOfSquares += component**2
        return math.sqrt(sumOfSquares)

    # using the caller, derives a new element of the Vector Space with length 1
    @abstractmethod
    def normalize(self):
        newObj = copy.copy(self)
        normValue = newObj.norm()
        if normValue == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        newObj._components = [component/normValue for component in self._components]
        return newObj
