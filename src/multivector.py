from src import vector, bivector, pseudoscalar


class Multivector():

    # these parameters are the coefficients
    def __init__(self, scalar, vector: vector, bivector: bivector, pseudoscalar: pseudoscalar):
        self._scalar = scalar
        self._vector = vector
        self._bivector = bivector
        self._pseudoscalar = pseudoscalar

    def __str__(self):
        print("scalar: ", self._scalar, "\n",
              "vector: ", self._vector, "\n",
              "bivector: ", self._bivector, "\n",
              "pseudoscalar: ", self._pseudoscalar)