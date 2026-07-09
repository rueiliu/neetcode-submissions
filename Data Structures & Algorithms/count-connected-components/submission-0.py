'''
create a list which contans sublist to store nodes and their edges
create a list(visit) with all values set to False(to mark have we seen this edge yet)
put nodes and edges into the list, and then write dfs funtion

in dfs, write a for loop that check if the edges have been checked, mark those checked with True

then use for loop and apply dfs through everything




'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)

        def dfs(node):

            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1

        return res


        