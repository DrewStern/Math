from abc import ABCMeta, abstractmethod
import copy
import math


# abstract class representing a Vector Space with an unknown number of dimensions
from src.Tools import Tools


class VectorSpace:
    __metaclass__ = ABCMeta

    # override the + operator for elements of the Vector Space
    @abstractmethod
    def __add__(self, other):
        if Tools.are_not_same_type(self, other):
            raise TypeError("Elements must be of the same type.")
        if Tools.are_not_same_length(self._components, other._components):
            raise IndexError("Elements must be of the same dimension.")
        newObj = copy.copy(self)
        newObj._components = [selfVal + otherVal for (selfVal, otherVal) in zip(self._components, other._components)]
        return newObj

    @abstractmethod
    def __radd__(self, other):
        return self + other

    # override the - operator for elements of the Vector Space
    @abstractmethod
    def __sub__(self, other):
        if Tools.are_not_same_type(self, other):
            raise TypeError("Elements must be of the same type.")
        if Tools.are_not_same_length(self._components, other._components):
            raise IndexError("Elements must be of the same dimension.")
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

    # calculates the magnitude of the caller
    @abstractmethod
    def norm(self):
        return math.sqrt(sum(component ** 2 for component in self._components))

    # using the caller, derives a new element of the Vector Space with magnitude 1
    @abstractmethod
    def normalize(self):
        newObj = copy.copy(self)
        normValue = newObj.norm()
        if normValue == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        newObj._components = [component / normValue for component in self._components]
        return newObj
