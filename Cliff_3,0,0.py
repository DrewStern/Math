from Bivector import Bivector
from Pseudoscalar import Pseudoscalar
from Vector import Vector


# Algebra of Physical Space
@staticmethod
class APS(Vector):
    class Multivector():

        # these parameters are the coefficients
        def __init__(self, scalar, vector, bivector, pseudoscalar):
            if type(vector) != Vector:
                raise TypeError("Vector parameter must be of Vector type.")

            if type(bivector) != Bivector:
                raise TypeError("Bivector parameter must be of Bivector type.")

            if type(pseudoscalar) != Pseudoscalar:
                raise TypeError("Pseudoscalar parameter must be of Pseudoscalar type.")

            self._scalar = scalar
            self._vector = vector
            self._bivector = bivector
            self._pseudoscalar = pseudoscalar

        def __str__(self):
            print("scalar: ", self._scalar, "\n",
                  "vector: ", self._vector, "\n",
                  "bivector: ", self._bivector, "\n",
                  "pseudoscalar: ", self._pseudoscalar)
