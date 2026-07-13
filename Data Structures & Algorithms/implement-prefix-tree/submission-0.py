class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:

        node = self.root

        for char in word:
            if char not in node.children and node.isEnd == False:
                return False
            node = node.children[char]
        
        return node.isEnd # not return True, cause I have to check if node.isEnd == True


    def startsWith(self, prefix: str) -> bool:
        
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True

        
        