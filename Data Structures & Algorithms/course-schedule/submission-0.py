


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
                #if 1 needs 0, and 0 needs 1 then a cycle is detected

            if preMap[crs] == []:
                return True

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []

            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True #if the classes are not linked