import unittest
import contiguous_array

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        nums = [0, 1]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 2)

    def test_2(self):
        nums = [0, 1, 0]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 2)

    def test_3(self):
        nums = [0, 1, 0, 1]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 4)

    def test_4(self):
        nums = [0, 1, 1, 0]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 4)

    def test_5(self):
        nums = [0, 1, 0, 1, 0, 0, 0]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 4)

    def test_6(self):
        nums = [0, 0, 0, 0, 1, 0, 1]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 4)
    
    def test_7(self):
        nums = [1]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 0)
    
    def test_8(self):
        nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
        sol = contiguous_array.Solution()
        res = sol.findMaxLength(nums)
        self.assertEqual(res, 68)

if __name__ == '__main__':
    unittest.main()