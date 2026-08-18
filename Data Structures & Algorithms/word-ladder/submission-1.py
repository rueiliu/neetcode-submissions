'''
BFS Search

1. check if endword is in wordlist, if not return 0
2. create adjacency list amd then add beginword into wordlist, create the adjacency list based on the wordlist(actuallt it's a dict)
3. BFS search set up, visit/q/res = 1
4. search in while q, if word == endword then return res, write a for loop that search for all adjency words


'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #adjacency list
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        # fill out the adjacency list
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word) 

        # set up BFS
        visit = set([beginWord])
        res = 1
        q = collections.deque([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            q.append(neighbor)
                            visit.add(neighbor)
            res += 1
        return 0
        


        