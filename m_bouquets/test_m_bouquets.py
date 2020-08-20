import unittest
import m_bouquets

class TestMBouquets(unittest.TestCase):
    def test_1(self):
        bloomDay = []
        m = 0
        k = 0

        sol = m_bouquets.Solution()
        res = sol.minDays(bloomDay, m, k)
        self.assertEqual(res, -1)

if __name__ == '__main__':
    unittest.main()