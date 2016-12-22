import unittest
import math
from Vector import Vector

class Vector_Test(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Vector, 'assertVectorsEqual')
        
        self.q = Vector(1, 10, 100)
        self.qNorm = math.sqrt(10101)
        
        self.p = Vector(2, 4, 8)
        self.pNorm = math.sqrt(84)

        self.long1 = Vector(1,2,3,4,5,6,7,8,9)
        self.long2 = Vector(9,8,7,6,5,4,3,2,1)

        self.unit_i = Vector(1, 0, 0)
        self.unit_j = Vector(0, 1, 0)
        self.unit_k = Vector(0, 0, 1)

    # tests both left and right addition
    def test_addition(self):
        self.assertEqual(self.q + self.p, Vector(3, 14, 108))
        self.assertEqual(self.p + self.q, Vector(3, 14, 108))

        self.assertEqual(self.long1 + self.long2, Vector(10,10,10,10,10,10,10,10,10))
        self.assertEqual(self.long2 + self.long1, Vector(10,10,10,10,10,10,10,10,10))

    def test_additionOfUnequalLengthVectorsRaisesException(self):
        with self.assertRaises(IndexError):
            self.q + self.long1
            self.long1 + self.q

    # tests both left and right subtraction
    def test_subtraction(self):
        self.assertEqual(self.q - self.p, Vector(-1, 6, 92))
        self.assertEqual(self.p - self.q, -Vector(-1, 6, 92))

    def test_subtractionOfUnequalLengthVectorsRaisesException(self):
        with self.assertRaises(IndexError):
            self.q - self.long1
            self.long1 - self.q

    def test_scalarMultiplication(self):
        self.assertEqual(3.3 * self.q, Vector(3.3, 33.0, 330.0))

    def test_scalarMultiplicationIsCommutative(self):
        self.assertEqual(self.p * 4, 4 * self.p)

    def test_scalarDivision(self):
        self.assertEqual(self.p / 8, Vector(.25, .5, 1))

    def test_dotProduct(self):
        self.assertEqual(self.q.dot(self.p), 842)

    def test_dotProductIsCommutative(self):
        self.assertEqual(self.q*self.p, self.p*self.q)

    def test_norm(self):
        self.assertEqual(self.q.norm(), self.qNorm)
        self.assertEqual(self.p.norm(), self.pNorm)

    def test_normalize(self):
        self.assertEqual(self.q.normalize(), self.q/self.qNorm)

    def test_crossProduct(self):
        self.assertEqual(self.q*self.p, Vector(-320, 192, -16))

    def test_crossProductIsAntiCommutative(self):
        self.assertEqual(self.q*self.p, -(self.p*self.q))

    def test_basisElementsAreOrthogonal(self):
        self.assertTrue(self.unit_i.is_orthogonal(self.unit_j))
        self.assertTrue(self.unit_j.is_orthogonal(self.unit_k))
        self.assertTrue(self.unit_k.is_orthogonal(self.unit_i))

    def test_collinearVectors(self):
        self.assertTrue(self.unit_i.is_collinear(self.unit_i))
        self.assertTrue(self.unit_i.is_collinear(-self.unit_i))

    def test_scalarTripleProduct(self):
        crossProduct = self.unit_j*self.unit_k # result is unit_i
        scalarTripleProduct = self.unit_i.dot(crossProduct)
        self.assertEqual(scalarTripleProduct, self.unit_i.norm())

    def assertVectorsEqual(self, q, p, msg=None):
        return all(qVal == pVal for qVal, pVal in zip(q._components, p._components))
