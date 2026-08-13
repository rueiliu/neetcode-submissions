'''
Understanding:
input: will be a 2d array
output: also a 2d array that stores 
find distance nearest treasure chest

Match:
BFS Search problem

Plan:
1. variable: rows(row length of the grid)/cols(col len of grid)/visit(grid that has been visited)
q(deque for bfs search), dist(to store the distance to treasure chest)

2. a double for loop that put all 0 into q, also set all treasure chest cell to 0(distance)

3. bfs search, go through all cell in q, and apply helper function(that checkes if cell can be transversed) for bfs search)
for each layer, add dist by 1

Review:

Evaluate:

'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        dist = 0

        def addgrid(r, c):
            if ( r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1 ):
                return
            q.append((r, c))
            visit.add((r, c))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
                    
        while q:

            # has different layers
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addgrid(r + 1, c)
                addgrid(r - 1, c)
                addgrid(r, c + 1)
                addgrid(r, c - 1)
            dist += 1








        