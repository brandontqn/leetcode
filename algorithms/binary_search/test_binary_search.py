import unittest
import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_1(self):
        target = 4
        arr = [0, 1, 2, 3, 4, 5]
        res = binary_search.binarySearch(target, arr)
        self.assertEqual(res, 4)

    def test_2(self):
        target = 1
        arr = [0, 1]
        res = binary_search.binarySearch(target, arr)
        self.assertEqual(res, 1)

    def test_3(self):
        target = 0
        arr = [0, 1]
        res = binary_search.binarySearch(target, arr)
        self.assertEqual(res, 0)

    def test_4(self):
        target = 2
        arr = [0, 1]
        res = binary_search.binarySearch(target, arr)
        self.assertEqual(res, -1)

if __name__ == '__main__':
    unittest.main()