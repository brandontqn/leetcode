import unittest
import word_ladder

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        sol = word_ladder.Solution()
        res = sol.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(res, 5)

if __name__ == '__main__':
    unittest.main()