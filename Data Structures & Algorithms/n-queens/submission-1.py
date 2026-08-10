'''
backtracking problem

solve diagonal by adding, deducting the rows and cols(bc if on same diagonal the sum would be all the same)

queens can attack each other if on the same row, column or diagonal

create 3 sets that store col, diagonal, negdiagonal
first need to set up the board then backtracking->basecase->iterate through each location and if the specific col or diagnoal are being placed already

then backtracking...



'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diagonal = set() # (r+c)
        negdiagonal = set() #(r-c)

        #the result
        res = []
        
        #layout the board
        board = [["."] * n for i in range(n)]

        def backtrack(r): # n is column
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy.copy())
                return

            for c in range(n):
                if c in col or (r + c) in diagonal or (r - c) in negdiagonal:
                    continue

                col.add(c)
                diagonal.add(r+c)
                negdiagonal.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)
                # if use stack, the pop sequence will be random
                col.remove(c)
                diagonal.remove(r + c)
                negdiagonal.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

                


 




        