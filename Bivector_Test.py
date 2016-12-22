import unittest
from Bivector import Bivector

class Bivector_Test(unittest.TestCase):
    def test_orientation(self):
        bv = Bivector(7, 4)
        self.assertTrue(bv.get_orientation());


if __name__ == '__main__':
    unittest.main()
