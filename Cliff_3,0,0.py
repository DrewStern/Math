import math
from Vector import Vector
from Bivector import Bivector
from Pseudoscalar import Pseudoscalar

# Algebra of Physical Space
@staticmethod
class APS(Vector):



    class Multivector():

        # these parameters are the coefficients
        def __init__(self, scalar, vector, bivector, pseudoscalar):
            self._scalar = scalar
            self._vector = Vector()
            self._bivector = Bivector()
            self._pseudoscalar = Pseudoscalar()

        def __str__(self):
            print("scalar: ", self._scalar, "\n",
              "vector: ", self._vector, "\n",
              "bivector: ", self._bivector, "\n",
              "pseudoscalar: ", self._pseudoscalar)