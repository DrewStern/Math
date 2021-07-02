import unittest

from src.multivector import Multivector


class ThreespaceAlgebraTestCases(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(Multivector, 'assertMultivectorsEqual')

    # tests both left and right addition
    def test_addition(self):
        pass

    def assertMultivectorsEqual(self, q, p, msg=None):
        return q._scalar == p._scalar and q._vector == p._vector and q._bivector == p._bivector and q._pseudoscalar == p._pseudoscalar
