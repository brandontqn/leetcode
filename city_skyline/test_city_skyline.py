import unittest
import city_skyline

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
        sol = city_skyline.Solution()
        res = sol.maxIncreaseKeepingSkyline(grid)
        self.assertEqual(res, 35)

if __name__ == '__main__':
    unittest.main()