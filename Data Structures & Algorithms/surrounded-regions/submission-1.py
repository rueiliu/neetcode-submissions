'''
Input: a list of list(matrix)
Output: a list of list(matrix)
transform the surrounded regions("O") into ("X")
not surrounded->remain the same

pseudocode:
BFS problem
1. go through all cells and mark the "O" that are along the edges
2. BFS algorithm and start expanding from the cells that we marked in the first step(mark them as "T")
3. iterate through all  the cells, and transform "T" into "O", while "O" to "X"


'''



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        # mark the "O" that are along the edges
        def scan():
            # double for loop to scam
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == 0 or c == 0 or r == (ROWS - 1) or c == (COLS - 1)) and board[r][c] == "O":
                        q.append((r, c))
                        board[r][c] = "T"
                    

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if (r + dr) < 0 or (c + dc) < 0 or (r + dr) == ROWS or (c+dc) == COLS or board[r + dr][c + dc] != "O":
                        continue
                    q.append((r + dr, c + dc))
                    board[r + dr][c + dc] = "T"

        scan()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"


