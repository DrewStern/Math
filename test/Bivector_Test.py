import unittest
from src.Vector import Vector
from src.Bivector import Bivector


class Bivector_Test(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Vector, 'assertVectorsEqual')
        self.addTypeEqualityFunc(Bivector, 'assertBivectorsEqual')

        # standard Euclidean basis elements
        self.unit_i = Vector(1, 0, 0)
        self.unit_j = Vector(0, 1, 0)
        self.unit_k = Vector(0, 0, 1)

        self.unit_ij = Bivector(self.unit_i, self.unit_j)
        self.unit_jk = Bivector(self.unit_j, self.unit_k)
        self.unit_ki = Bivector(self.unit_k, self.unit_i)

        self.unit_ji = self.unit_ij.reverse()
        self.unit_kj = self.unit_jk.reverse()
        self.unit_ik = self.unit_ki.reverse()

    def test_nonVectorParameterRaisesTypeError(self):
        with self.assertRaises(TypeError):
            Bivector(Vector(1, 0, 0), 1)
            Bivector(1, Vector(1, 0, 0))

    def test_area(self):
        self.assertEquals(self.unit_ij.area(), 1)
        self.assertEquals(self.unit_jk.area(), 1)
        self.assertEquals(self.unit_ki.area(), 1)

    def test_orientation(self):
        self.assertEquals(self.unit_ij.orientation(), self.unit_i * self.unit_j)

    def test_dual(self):
        self.assertEquals(self.unit_ij.dual(), self.unit_k)
        self.assertEquals(self.unit_jk.dual(), self.unit_i)
        self.assertEquals(self.unit_ki.dual(), self.unit_j)

        self.assertEquals(self.unit_ji.dual(), -self.unit_k)
        self.assertEquals(self.unit_kj.dual(), -self.unit_i)
        self.assertEquals(self.unit_ik.dual(), -self.unit_j)

    def assertVectorsEqual(self, q, p, msg=None):
        return all(qVal == pVal for qVal, pVal in zip(q._components, p._components))

    def assertBivectorsEqual(self, q, p, msg=None):
        return q._e1 == p._e1 and q._e2 == p._e2
