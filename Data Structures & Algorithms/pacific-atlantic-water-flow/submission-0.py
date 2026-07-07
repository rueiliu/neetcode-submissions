'''
Apply DFS search and store feasible solution in two sets, pac, atl and if one coordinates exist in both


iterate from the first row near pac 
iterate from the first row near atl 
bc if get close the the first line then can get to ocean for sure



'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, previousHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r == ROW or c == COL
            or heights[r][c] < previousHeight):
                return

            visit.add((r,c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])


        
        
        
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW-1, c, atl, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL-1, atl, heights[r][COL-1])

        res = []

        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res





        


        