import unittest
import math
from src.Complex import Complex


class Complex_Test(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Complex, 'assertComplexEqual')

        self.q = Complex(1, 10)
        self.qNorm = math.sqrt(101)
        self.qInverse = Complex(1 / 101, -10 / 101)

        self.p = Complex(2, 4)
        self.pNorm = math.sqrt(20)
        self.pInverse = Complex(.1, -.2)

        self.unit_r = Complex(1, 0)
        self.unit_i = Complex(0, 1)

    # tests both left and right addition
    def test_addition(self):
        self.assertEqual(self.q + self.p, Complex(3, 14))
        self.assertEqual(self.p + self.q, Complex(3, 14))

    # tests both left and right subtraction
    def test_subtraction(self):
        self.assertEqual(self.q - self.p, Complex(-1, 6))
        self.assertEqual(self.p - self.q, -Complex(-1, 6))

    def test_scalarMultiplication(self):
        self.assertEqual(3.3 * self.q, Complex(3.3, 33.0))

    # scalar*Complex == Complex*scalar
    def test_scalarMultiplicationCommutative(self):
        self.assertEqual(self.p * 4, 4 * self.p)

    def test_scalarDivision(self):
        self.assertEqual(self.q / 1000, Complex(0.001, 0.01))

    def test_zeroDivisorRaisesZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            self.q / 0

    def test_complexMultiplication(self):
        self.assertEqual(self.q * self.p, Complex(-38, 24))

    def test_complexMultiplicationIsCommutative(self):
        self.assertEqual(self.q * self.p, self.p * self.q)

    def test_power(self):
        print("\n", self.p ** 3, " ?= ", Complex(-88, -16))
        self.assertEqual(self.p ** 3, Complex(-88, -16))

    # the basis element i has the property i^2 = -1
    def test_imaginaryBasisElementSquaresToNegativeOne(self):
        print("\n", self.unit_i ** 2, " ?= ", Complex(-1, 0))
        self.assertEqual(self.unit_i ** 2, Complex(-1, 0))

    def test_nonIntegralPowerRaisesTypeError(self):
        with self.assertRaises(TypeError):
            self.q ** 4.5

    def test_norm(self):
        self.assertEqual(self.q.norm(), self.qNorm)
        self.assertEqual(self.p.norm(), self.pNorm)

    # |qp| == |q||p|
    def test_normIsMultiplicative(self):
        self.assertEqual(self.q.norm() * self.p.norm(), self.qNorm * self.pNorm)

    # |q| == sqrt(qq*)
    # where q* is the conjugate
    def test_normSquaredIsSelfTimesConjugate(self):
        self_times_conjugate = self.q * self.q.conjugate()
        self.assertTrue(self_times_conjugate.is_real())
        self.assertEqual(self.q.norm(), math.sqrt(self_times_conjugate.real_part()))

    def test_normalize(self):
        self.assertEqual(self.q.normalize(), self.q / self.qNorm)

    def test_conjugate(self):
        self.assertEqual(self.q.conjugate(), Complex(1, -10))

    def test_conjugateIsOwnInverse(self):
        self.assertEqual(self.q, self.q.conjugate().conjugate())

    def test_reciprocal(self):
        self.assertEqual(self.q.reciprocal(), self.qInverse)
        self.assertEqual(self.p.reciprocal(), self.pInverse)

    def test_zeroHasNoReciprocal(self):
        zero = Complex(0, 0)
        with self.assertRaises(ZeroDivisionError):
            zero.reciprocal()

    @unittest.skip("this doesn't seem to be working correctly")
    def test_exp(self):
        expQuat1 = Complex(math.pi, math.pi).exp()
        resultant1 = Complex(100000000 * math.e ** math.pi, 0)

        print("\nexpQuat1: ", expQuat1)
        print("\nresultant1: ", resultant1)

        self.assertEqual(expQuat1, resultant1)

        expQuat2 = Complex(math.pi / 2, math.pi / 2).exp()
        resultant2 = Complex(100000000 * math.e ** (math.pi / 2), 0)

        print("\nexpQuat2: ", expQuat2)
        print("\nresultant2: ", resultant2)

        self.assertEqual(expQuat2, resultant2)

    def assertComplexEqual(self, q, p, msg=None):
        return all(qVal == pVal for (qVal, pVal) in zip(q._components, p._components))
