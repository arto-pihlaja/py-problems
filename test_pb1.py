import unittest
import pb1
class TestFirstProb(unittest.TestCase):
    def test_simple(self):
        tstArr = [-1, -1, 0, 1, 2]
        self.assertEqual(pb1.calculateRatios(tstArr), [0.4, 0.4, 0.2])

    def test_rounding(self):
        tstArr = [-1, 5, -1, 0, 1, 2]
        self.assertEqual(pb1.calculateRatios(tstArr), [0.5000, 0.333333, 0.166667])

if __name__ == "__main__":
    unittest.main()
