import pb2
import unittest

class TestPb2(unittest.TestCase):
    def test_simple_case(self):
        arr = [1, 8, 3, 2, 7, 4]
        self.assertEqual(pb2.findIndices(arr, 12),(1,5),"Failed to find indices of suitable positive int")

    def test_with_neg_int(self):
        arr = [1, 8, 5, 2, 7, -4]
        self.assertEqual(pb2.findIndices(arr, 4),(1,5),"Failed to find indices of suitable int")

if __name__ == "__main__":
    unittest.main()