import unittest
import math
from APS import APS
from PolyVector import PolyVector

class APS_Test(unittest.TestCase):

    def setUp(self):
        self.addTypeEqualityFunc(PolyVector, 'assertPolyVectorsEqual')

    # tests both left and right addition
    def test_addition(self):

    def assertPolyVectorsEqual(self, q, p, msg=None):
        return q._scalar == p._scalar and q._vector == p._vector and q._bivector == p._bivector and q._pseudoscalar == p._pseudoscalar
