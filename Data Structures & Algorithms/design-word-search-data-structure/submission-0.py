'''
set up a trie class

then



'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.EndOfWord = True
        
    # . must match with the letters that have already exists in the trienode
    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            curr = root    

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for string in curr.children.values():
                        if dfs(i+1, string):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.EndOfWord

        return dfs(0, self.root)
        
