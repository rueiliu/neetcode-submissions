'''
prim's algorithm + minheap

always pick the edge with lowest distance till all points are connected
use length to check if all points have been connected



'''


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visit = set()
        res = 0
        minheap = [(0, 0)]
        n = len(points)

        while len(visit) < n:
            dist, i = heapq.heappop(minheap)

            if i in visit:
                continue

            visit.add(i)
            res += dist

            x1, y1 = points[i]

            for j in range(n):
                if j not in visit:
                    x2, y2 = points[j]
                    length = abs(x1-x2) + abs(y1-y2)
                    
                    heapq.heappush(minheap, (length, j))


        return res


        