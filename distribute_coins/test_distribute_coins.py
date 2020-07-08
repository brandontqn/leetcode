import unittest
import distribute_coins

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        valList = [3, 0, 0]
        sol = distribute_coins.Solution()
        tree = sol.createBinaryTree(valList)
        res = sol.distributeCoins(tree[0])
        self.assertEqual(res, 2)

if __name__ == '__main__':
    unittest.main()