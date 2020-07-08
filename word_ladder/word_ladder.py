# https://leetcode.com/problems/word-ladder/solution/

# 127. Word Ladder

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

class Solution:
    graph = dict()
        
    def ladderLength(self, beginWord, endWord, wordList):
        if(endWord not in wordList):
            return 0
        
        self.buildGraph(beginWord, endWord, wordList)
        return self.breadFirstSearch(beginWord, endWord, wordList)
    
    def buildGraph(self, beginWord, endWord, wordList):
        wordLength = len(beginWord)
        self.graph[beginWord] = list()
        
        for word in wordList:
            self.graph[word] = list()
            
        for key in self.graph.keys():
            for word in wordList:
                if(key == word):
                    continue
                    
                diff = 0
                for i in range(wordLength):
                    if(key[i] != word[i]):
                        diff += 1
                                        
                if(diff == 1):
                    self.graph[key].append(word)
                    
    def breadFirstSearch(self, beginWord, endWord, wordlist):
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        
        while(queue):
            current_word, level = queue.pop(0)
            for neighbour in self.graph[current_word]:
                if(neighbour == endWord):
                    return level + 1
                
                if(neighbour not in visited):
                    visited[neighbour] = True
                    queue.append((neighbour, level + 1))
        return 0