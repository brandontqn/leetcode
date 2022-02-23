"""
imp, [impossible, imp, ipod, elf, ipad]

=> [[imp, impossible, ipad], [imp, impossible], [imp, impossible]]
"""
from collections import deque

class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}

class Trie(object):
    def __init__(self, repository):
        self.root = TrieNode()
        self.buildTrie(repository)

    def buildTrie(self, words):
        for word in words:
            self.addWord(word)

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char] 
        curr.word = word

    def findNeighbours(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        return self.bfs(curr)

    def bfs(self, root):
        if not root:
            return []
        neighbours = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node.word:
                neighbours.append(node.word)
            for child in node.children.values():
                q.append(child)
        return neighbours

def wordSuggestion(s, repository):
    t = Trie(repository)
    n = len(s)
    res = []
    for i in range(n):
        prefix = s[0:i+1]
        neighbours = t.findNeighbours(prefix)
        sorted_neighbors = sorted(neighbours)
        m = len(sorted_neighbors)
        arr = [sorted_neighbors[i] for i in range(3)] if m > 2 else [sorted_neighbors[i] for i in range(m)]
        res.append(arr)
    return res

def main():
    s = "imp"
    repository = ["impossible", "imp", "ipod", "elf", "ipad"]
    result = wordSuggestion(s, repository)
    print(result)

if __name__ == "__main__":
    main()