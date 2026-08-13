'''
input: 2D grid
output: integer, -1 if cant' find a solution


1. create variable row, col, visits, q(bfs), fresh(calculate how many fresh fruit there still are), time
2. scan through the grid, add fresh fruit into q, store rot fruit to rot_r, rot_c
3. apply bfs algo , for each iteration deduct fresh count

time: O(m x n)
space: O(mn)


'''


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        time = 0
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        # scan through the grid to put rotten fruit into q

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
               

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
        
                    # skip this cell bc no fresh fruit
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or
                     grid[row][col] != 1):
                        continue

                    q.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1

            time += 1

            
        return time if fresh == 0 else -1

                


                    

            

                

        