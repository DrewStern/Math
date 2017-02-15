import unittest
import math
from Vector import Vector

class Vector_Test(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Vector, 'assertVectorsEqual')

        # consecutive powers of 10
        self.q = Vector(1, 10, 100)
        self.qNorm = math.sqrt(10101)

        # consecutive powers of 2
        self.p = Vector(2, 4, 8)
        self.pNorm = math.sqrt(84)

        # 10-dimensional Vectors
        self.long1 = Vector(1,2,3,4,5,6,7,8,9)
        self.long2 = Vector(9,8,7,6,5,4,3,2,1)

        # standard Euclidean basis elements
        self.unit_i = Vector(1, 0, 0)
        self.unit_j = Vector(0, 1, 0)
        self.unit_k = Vector(0, 0, 1)

    # Calculates both left and right addition.
    def test_addition(self):
        self.assertEqual(self.q + self.p, Vector(3, 14, 108))
        self.assertEqual(self.p + self.q, Vector(3, 14, 108))

        self.assertEqual(self.long1 + self.long2, Vector(10,10,10,10,10,10,10,10,10))
        self.assertEqual(self.long2 + self.long1, Vector(10,10,10,10,10,10,10,10,10))

    # Ensures that we can't add Scalars to Vectors.
    def test_additionOfVectorWithNonvectorRaisesException(self):
        with self.assertRaises(TypeError):
            self.q + 1
            1 + self.q

    # Ensures that we can't add Vectors of different dimensionality.
    def test_additionOfUnequalLengthVectorsRaisesException(self):
        with self.assertRaises(IndexError):
            self.q + self.long1
            self.long1 + self.q

    # Calculates both left and right subtraction.
    def test_subtraction(self):
        self.assertEqual(self.q - self.p, Vector(-1, 6, 92))
        self.assertEqual(self.p - self.q, -Vector(-1, 6, 92))

    # Ensures that we can't subtract Scalars from Vectors.
    def test_subtractionOfVectorWithNonvectorRaisesException(self):
        with self.assertRaises(TypeError):
            self.q + 1
            1 + self.q

    # Ensures that we can't subtract Vectors of different dimensionality.
    def test_subtractionOfUnequalLengthVectorsRaisesException(self):
        with self.assertRaises(IndexError):
            self.q - self.long1
            self.long1 - self.q

    # Calculates left multiplication by a Scalar.
    def test_scalarMultiplication(self):
        self.assertEqual(3.3 * self.q, Vector(3.3, 33.0, 330.0))
        self.assertEqual(4.5 * self.p, Vector(9.0, 18.0, 36.0))

    # Ensures that Scalar multiplication from the left is the same as from the right.
    def test_scalarMultiplicationIsCommutative(self):
        self.assertEqual(self.q * 9.8, 9.8 * self.p)
        self.assertEqual(self.p * 4, 4 * self.p)

    # Ensures that Scalar multiplication is distributed correctly.
    def test_scalarMultiplicationIsDistributive(self):
        self.assertEqual(4 * (self.q + self.p), Vector(12, 56, 432))
        self.assertEqual(3 * (self.p - self.q), Vector(3, -18, -276))

    # Calculates division by a Scalar.
    def test_scalarDivision(self):
        self.assertEqual(self.q / .5, Vector(2, 20, 200))
        self.assertEqual(self.p / 8, Vector(.25, .5, 1))

    # Calculates the Dot product between two Vectors.
    def test_dotProduct(self):
        self.assertEqual(self.q.dot(self.p), 842)

    # Ensures that the Dot product is commutative.
    def test_dotProductIsCommutative(self):
        self.assertEqual(self.q.dot(self.p), self.p.dot(self.q))

    # Ensures that the Dot product is only calculated between two Vectors.
    def test_dotProductOfVectorWithNonvectorRaisesException(self):
        with self.assertRaises(TypeError):
            self.q.dot(1)

    # Ensures that the Dot product is only calculated between two Vectors of same dimensionality.
    def test_dotProductOfUnequalLengthVectorsRaisesException(self):
        with self.assertRaises(IndexError):
            self.q.dot(self.long1)

    def test_norm(self):
        self.assertEqual(self.q.norm(), self.qNorm)
        self.assertEqual(self.p.norm(), self.pNorm)

    def test_normalize(self):
        self.assertEqual(self.q.normalize(), self.q / self.qNorm)

    def test_crossProduct(self):
        self.assertEqual(self.q.cross(self.p), Vector(-320, 192, -16))

    def test_crossProductIsAntiCommutative(self):
        self.assertEqual(self.q.cross(self.p), -(self.p.cross(self.q)))

    def test_basisElementsAreOrthogonal(self):
        self.assertTrue(self.unit_i.is_orthogonal(self.unit_j))
        self.assertTrue(self.unit_j.is_orthogonal(self.unit_k))
        self.assertTrue(self.unit_k.is_orthogonal(self.unit_i))


    # TODO: write unit tests for the angle_between method


    def test_parallelVectors(self):
        self.assertTrue(self.unit_i.is_parallel(self.unit_i))

    def test_antiparallelVectors(self):
        self.assertTrue(self.unit_i.is_antiparallel(-self.unit_i))

    def test_scalarTripleProduct(self):
        crossProduct = self.unit_j.cross(self.unit_k) # result is unit_i
        scalarTripleProduct = self.unit_i.dot(crossProduct)
        self.assertEqual(scalarTripleProduct, self.unit_i.norm())

    def assertVectorsEqual(self, q, p, msg=None):
        return all(qVal == pVal for qVal, pVal in zip(q._components, p._components))
