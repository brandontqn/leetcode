import unittest
import satisfiability_of_equality_equations

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        equations = ['a==b', 'b!=a']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(equations)
        self.assertEqual(res, False)
    
    def test_2(self):
        equations = ['b==a', 'a==b']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(equations)
        self.assertEqual(res, True)

    def test_3(self):
        equations = ['a==b', 'b==c', 'a==c']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(equations)
        self.assertEqual(res, True)

    def test_4(self):
        equations = ['a==b', 'b!=c', 'c==a']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(equations)
        self.assertEqual(res, False)

    def test_5(self):
        equations = ['c==c', 'b==d', 'x!=z']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(equations)
        self.assertEqual(res, True)

    def test_6(self):
        equations = ['a!=a']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(equations)
        self.assertEqual(res, False)

    def test_7(self):
        equations = ['a==b', 'e==c', 'b==c', 'a!=e']
        sol = satisfiability_of_equality_equations.Solution()
        res = sol.equationsPossible(equations)
        self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()