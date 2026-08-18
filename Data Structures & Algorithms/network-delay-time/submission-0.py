'''


dfs

1. create a hashmap and store times in it(start is key, end and time are value)
2. create another dist with default(inf) value, and write a helper function that will run the stored times  
into it, if one node is being reached, then replace the inf with the actual value
3. if no inf in dist then return the maxium value else -1
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}


        def dfs(node, time):
            if time >= dist[node]:
                return

            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w)


        dfs(k, 0)
        res = max(dist.values())
        return res if res < float("inf") else -1        