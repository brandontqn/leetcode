class TrieNode(object):
    def __init__(self, word = None, children = {}):
        self.word = word
        self.children = children

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr = self.root
        n = len(key)

        for i in range(n):
            if key[i] not in curr.children:
                curr.children[key[i]] = TrieNode()
            curr = curr.children[key[i]]
        curr.word = key

    def search(self, key):
        curr = self.root
        n = len(key)

        for i in range(n):
            if key[i] not in curr.children:
                return False
            curr = curr.children[key[i]]

        return curr.word != None

    def findAllWords(self, node):
        pass