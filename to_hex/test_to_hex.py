import unittest
import to_hex

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        num = 26
        sol = to_hex.Solution()
        res = sol.toHex(num)
        self.assertEqual(res, '1a')

    def test_2(self):
        num = -1
        sol = to_hex.Solution()
        res = sol.toHex(num)
        self.assertEqual(res, 'ffffffff')

    def test_3(self):
        num = -5
        sol = to_hex.Solution()
        res = sol.toHex(num)
        self.assertEqual(res, 'fffffffb')

    def test_4(self):
        num = 50
        sol = to_hex.Solution()
        res = sol.toHex(num)
        self.assertEqual(res, '32')

if __name__ == '__main__':
    unittest.main()