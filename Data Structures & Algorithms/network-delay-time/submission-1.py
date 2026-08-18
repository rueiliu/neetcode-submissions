'''
dijkstra(BFS+heap)

1. create hashmap of times
2. set up minheap/visit/t
3. while minheap(time) exist, pop w1, n1 out and check if n1 in visit(if it does then continue, bc want to avoid cycle)
4. max(t, w1)
5. BFS- go throught the neighbors of n1 and if new visit push it into heap(time is accumulated)
6. return t





'''


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge = collections.defaultdict(list)
        for u, v, t in times:
            edge[u].append((v, t))

        minheap = [(0 ,k)]
        visit = set()
        t = 0

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue

            visit.add(n1)
            t = max(t, w1)

            # check the neighbors
            for n2, w2 in edge[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1+w2, n2))

        return t if len(visit) == n else -1
        