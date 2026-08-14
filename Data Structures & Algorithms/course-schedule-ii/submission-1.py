'''
input: array of lists, second element is the prerequisites of the first element
output: an array(all courses we need to take to fullfill numcourses) if can not fulfull, return empty list


pseudocode:
DFS problem, and we need to detetc if a cycle exists, if exists then return [], else courses
variable: result []/visited set()(courses that have been checked and are feasible to take)/ cycle set() current prerequisites that dfs is checking
1. create a hashmap that stores the prerequisites
2. write a dfs helper function which will go through every prerequisites.
    a.first check if prereq is in cycle, if it is return False
    b. check if prereq in visit, if it is then return True
    c. use a for loop to check the all the prereq with calling the dfs to see if any of them return False
    d. remove current element from cycle, add it to visit and result and return True

3. write another loop that iterate through all classes and call dfs, if there's False return [], else result[]


time complexity: O(number of course + prereq )
space complexity: O(number of course + prereq )

'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create hashmap
        coursemap = {i:[] for i in range(numCourses)} 
        #put all of the courses and their corresponding prereq in it
        for course, prereq in prerequisites:
            coursemap[course].append(prereq)
        
        result = []
        visit = set()
        cycle = set()

        def dfs(c):
            # cycle detected
            if c in cycle:
                return False
            # if the element has been checked before
            if c in visit:
                return True
            # add the current element into cycle
            cycle.add(c)
            # check all prereq
            for pre in coursemap[c]:
                if not dfs(pre):
                    return False

            cycle.remove(c)
            visit.add(c)
            result.append(c)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result

    


        