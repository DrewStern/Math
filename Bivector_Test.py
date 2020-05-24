import unittest
from Vector import Vector
from Bivector import Bivector


class Bivector_Test(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Bivector, 'assertBivectorsEqual')

        # standard Euclidean basis elements
        self.unit_i = Vector(1, 0, 0)
        self.unit_j = Vector(0, 1, 0)
        self.unit_k = Vector(0, 0, 1)

    def test_nonVectorParameterRaisesTypeError(self):
        with self.assertRaises(TypeError):
            Bivector(Vector(1, 0, 0), 1)
            Bivector(1, Vector(1, 0, 0))

    def test_orientation(self):
        bv = Bivector(self.unit_i, self.unit_j)
        self.assertTrue(bv.orientation(), self.unit_i * self.unit_j);

    def assertBivectorsEqual(self, q, p, msg=None):
        return all(qVal == pVal for qVal, pVal in zip(q._components, p._components))
