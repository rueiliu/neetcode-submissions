'''
Trie is a tree structure for strings.

for init, there will be two properties-children(for each letter) and endofword(boolean) to store the status of the string

for insert, set curr as root, then use for loop. When string is not in curr.children, creat a new Trienode, if it exists, move curr to this node
at the end set endofword as true

for search, set curr as root, then use for loop. When string is not in curr.children, return False. 
update curr to the current node, then return curr.endofword(if the current node is the endofword it will return true)

for startswith, set curr as root, then use for loop. When string is not in curr.children, return False. move curr everytime
then at the end return true

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.EndOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.EndOfWord
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
             
        
        