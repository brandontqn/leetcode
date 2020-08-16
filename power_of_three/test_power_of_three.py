import unittest
import power_of_three

class TestPowerOfThree(unittest.TestCase):
    def test_1(self):
        n = 1
        sol = power_of_three.Solution()
        res = sol.isPowerOfThree(n)
        self.assertEqual(res, True)

    def test_2(self):
        n = 3
        sol = power_of_three.Solution()
        res = sol.isPowerOfThree(n)
        self.assertEqual(res, True)
    
    def test_3(self):
        n = 6
        sol = power_of_three.Solution()
        res = sol.isPowerOfThree(n)
        self.assertEqual(res, False)    
    
    def test_4(self):
        n = 9
        sol = power_of_three.Solution()
        res = sol.isPowerOfThree(n)
        self.assertEqual(res, True)    

if __name__ == '__main__':
    unittest.main()