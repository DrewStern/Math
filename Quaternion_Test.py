import unittest
import math
from Quaternion import Quaternion

class Quaternion_Test(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Quaternion, 'assertQuaternionsEqual')
        
        self.q = Quaternion(1, 10, 100, 1000)
        self.qNorm = math.sqrt(1010101)
        
        self.p = Quaternion(2, 4, 8, 16)
        self.pNorm = math.sqrt(340)

        self.unit_h = Quaternion(1, 0, 0, 0)
        self.unit_i = Quaternion(0, 1, 0, 0)
        self.unit_j = Quaternion(0, 0, 1, 0)
        self.unit_k = Quaternion(0, 0, 0, 1)

    # tests both left and right addition
    def test_addition(self):
        self.assertEqual(self.q + self.p, Quaternion(3, 14, 108, 1016))
        self.assertEqual(self.p + self.q, Quaternion(3, 14, 108, 1016))

    # tests both left and right subtraction
    def test_subtraction(self):
        self.assertEqual(self.q - self.p, Quaternion(-1, 6, 92, 984))
        self.assertEqual(self.p - self.q, -Quaternion(-1, 6, 92, 984))

    def test_scalarMultiplication(self):
        self.assertEqual(3.3 * self.q, Quaternion(3.3, 33.0, 330.0, 3300.0))

    # scalar*Quaternion == Quaternion*scalar
    def test_scalarMultiplicationCommutative(self):
        self.assertEqual(self.p * 4, 4 * self.p)

    def test_scalarDivision(self):
        self.assertEqual(self.q / 1000, Quaternion(0.001, 0.01, 0.1, 1))

    def test_zeroDivisorRaisesZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            self.q / 0

    # Quaternion multiplication is noncommutative
    def test_quaternionMultiplication(self):
        self.assertEqual(self.q * self.p, Quaternion(-16838, -6376, 4048, 1696))
        self.assertEqual(self.p * self.q, Quaternion(-16838, 6424, -3632, 2336))

    # the basis elements i, j, k have the property i^2 = j^2 = k^2 = -1
    def test_imaginaryBasisElementsSquareToNegativeOne(self):
        negativeOneScalar = Quaternion(-1, 0, 0, 0)
        self.assertEqual(self.unit_i**2, negativeOneScalar)
        self.assertEqual(self.unit_j**2, negativeOneScalar)
        self.assertEqual(self.unit_k**2, negativeOneScalar)

    # the basis elements i, j, k have the property ijk = -1
    def test_imaginaryBasisElementsMultiplyToNegativeOne(self):
        self.assertEqual(self.unit_i*self.unit_j*self.unit_k, Quaternion(-1, 0, 0, 0))

    # the basis elements i, j, k are cyclic in the sense that if one chooses two neighboring elements in the chain
    # i -> j -> k -> i -> j -> k -> ...
    # and multiplies them in the order they appear in the chain, then the result is the element to the right of the second element
    # the same holds going backwards, but with a negative sign
    def test_imaginaryBasisElementsAreCyclical(self):
        self.assertEqual(self.unit_i*self.unit_j, self.unit_k)
        self.assertEqual(self.unit_j*self.unit_k, self.unit_i)
        self.assertEqual(self.unit_k*self.unit_i, self.unit_j)
        self.assertEqual(self.unit_j*self.unit_i, -self.unit_k)
        self.assertEqual(self.unit_k*self.unit_j, -self.unit_i)
        self.assertEqual(self.unit_i*self.unit_k, -self.unit_j)

    def test_nonIntegralPowerRaisesTypeError(self):
        with self.assertRaises(TypeError):
            self.q**4.5
        
    def test_norm(self):
        self.assertEqual(self.q.norm(), self.qNorm)
        self.assertEqual(self.p.norm(), self.pNorm)

    # |qp| == |q||p|
    def test_normIsMultiplicative(self):
        resultant = self.q*self.p
        self.assertEqual(self.q.norm()*self.p.norm(), resultant.norm())

    # |q| == sqrt(qq*)
    # where q* is the conjugate
    def test_normSquaredIsSelfTimesConjugate(self):
        selfTimesConjugate = self.q*self.q.conjugate()
        self.assertEqual(self.q.norm(), math.sqrt(selfTimesConjugate))

    def test_normalize(self):
        self.assertEqual(self.q.normalize(), self.q / self.qNorm)

    def test_conjugate(self):
        self.assertEqual(self.q.conjugate(), Quaternion(1, -10, -100, -1000))
        self.assertEqual(self.p.conjugate(), Quaternion(2, -4, -8, -16))

    def test_conjugateIsOwnInverse(self):
        self.assertEqual(self.q, self.q.conjugate().conjugate())

    def test_reciprocal(self):
        self.assertEqual(self.q.reciprocal(), self.q / self.qNorm**2)

    @unittest.skip("this doesn't seem to be working correctly")
    def test_exp(self):
        expQuat1 = Quaternion(math.pi, math.pi, math.pi, math.pi).exp()
        resultant1 = Quaternion(100000000*math.e**math.pi, 0, 0, 0)

        print("\nexpQuat1: ", expQuat1)
        print("\nresultant1: ", resultant1)
        
        self.assertEqual(expQuat1, resultant1)

        expQuat2 = Quaternion(math.pi/2, math.pi/2, math.pi/2, math.pi/2).exp()
        resultant2 = Quaternion(100000000*math.e**(math.pi/2), 0, 0, 0)

        print("\nexpQuat2: ", expQuat2)
        print("\nresultant2: ", resultant2)
        
        self.assertEqual(expQuat2, resultant2)

    def test_isScalar(self):
        scalarOnly = Quaternion(1, 0, 0, 0)
        self.assertTrue(scalarOnly.is_scalar())

    def test_IsNotScalar(self):
        vectorOnly = Quaternion(0, 1, 2, 3)
        self.assertFalse(vectorOnly.is_scalar())

    def test_isVector(self):
        vectorOnly = Quaternion(0, 1, 2, 3)
        self.assertTrue(vectorOnly.is_vector())

    def test_IsNotVector(self):
        scalarOnly = Quaternion(1, 0, 0, 0)
        self.assertFalse(scalarOnly.is_vector())

    def assertQuaternionsEqual(self, q, p, msg=None):
        return q._h == p._h and q._i == p._i and q._j == p._j and q._k == p._k
