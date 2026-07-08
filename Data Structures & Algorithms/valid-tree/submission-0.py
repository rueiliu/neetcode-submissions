'''
undirected mean one node conneced to both nodes.

Use dfs search to check if it makes a valid tree

valid tree-> all nodes are connected and no cycle

create a hashmap to store n and edges, then use for loop to fill the data in

creats a visit set that store nodes that have been evaluated(if visited twice mean there are)

write the dfs function(i, prev), prev is to prevent false posiive of identifying a cycle

check if n in visit, if it does the return False

add i to visit

use a for loop that iterate through the edges of i and if they're in visit contine, else initiate dfs funtion

at the end start dfs function and also check if len(visit) == n




'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False

            return True

        return dfs(0,-1) and n == len(visit) # make sure all nodes are connected




        