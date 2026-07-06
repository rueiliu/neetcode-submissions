'''
use a Trienode, create a class and create a funtion that can insert word into the trienode

then in the findwords function, first extract rol, col and res() visit()
(result will store the final answer, while visit will store the current string that we're looking at(backtracking))
write a dfs function, that first will check if requirements are all met, then apply dfs search

then remove the current search location

write two for loop to search through the grid, run a thorough search


'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

    def insertword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.EndOfWord = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROW, COL = len(board), len(board[0])
        res, visit = set(), set() 
        root = TrieNode()
        for word in words:
            root.insertword(word)


        def dfs(r, c, node, word):
            
            if (r < 0 or c < 0 or r == ROW or c == COL or 
            board[r][c] not in node.children
            or (r,c)  in visit):
                return


            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.EndOfWord:
                res.add(word)


            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c))
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c, root, "")
        
        return list(res)


    



           