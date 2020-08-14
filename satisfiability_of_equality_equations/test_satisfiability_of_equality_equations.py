import unittest
import satisfiability_of_equality_equations

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        nums = ['a==b']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(nums)
        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()