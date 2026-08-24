'''
Understand:
Input: a list of lists
the questions: find the min of elevation
output: an integer

Match: 

Dijkstra + minheap problem

Implementation:
1. create visit set/ minheap / directions / time 

2. while minheap, first extract time, r, c from minheap, then check if r, c are at the dest, if it is return time

3. using a for loop that tries adding r,c with each direction, and if the new nodes are inside the range and have not been visited yet, push it into the heap and added to visit


'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        minheap = [(grid[0][0], 0, 0)]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        n = len(grid)
        visit.add((0,0))

        while minheap:
            time, r, c = heapq.heappop(minheap)

            #keep the maximum time 
            time = max(time, grid[r][c])

            if r == n-1 and c == n - 1 :
                return time

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr <= (n-1) and 0 <= nc <= (n-1) and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(minheap, (max(time, grid[nr][nc]), nr, nc))
        