class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree ={} # how many letters must come before this letter

        #add every character
        for word in words:
            for char in word:
                graph[char] = set()
                indegree[char] = 0

        for i in range(len(words)-1): # -1 bc to prevent out of index, i vs i+1
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            #check edge cases
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break


        q = deque([c for c in indegree if indegree[c]==0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            
        if len(res) != len(indegree):
            return ""

        return "".join(res)

