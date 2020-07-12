import unittest
import two_city_scheduling

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        costs = [[10,20],[30,200],[400,50],[30,20]]
        sol = two_city_scheduling.Solution()
        res = sol.twoCitySchedCost(costs)
        self.assertEqual(res, 110)

if __name__ == '__main__':
    unittest.main()