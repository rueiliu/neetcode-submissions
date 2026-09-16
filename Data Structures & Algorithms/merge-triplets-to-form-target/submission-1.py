'''
greedy solution

1. first create x,y,z, representing the integers in triplets respectively, ande set them into false
2. use a for loop to check if x,y,z equals to target, and if other elements in one triplet are greater than target, then its not gonna work as well
3. if x,y,z all equal to true than return true else return False 



'''


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
       
        x = y = z = False

        for t in triplets:

            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])

            if x and y and z:
                return True
        return False



