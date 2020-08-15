import unittest
import quicksort

class TestQuicksort(unittest.TestCase):
    def test_1(self):
        arr = [1, 3, 4, 5, 2, 0]
        res = quicksort.quickSort(arr)
        self.assertEqual(res, [0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()