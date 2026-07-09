'''
apply dynamic programming!
create two variable(previous, previous of previous)
with each is the sum of that current house
calculate the largest sum of the house

'''

class Solution:
    #house1, house2, n, n+1...
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0

        for n in nums:
            temp = max(n + house1, house2)
            house1 = house2
            house2 = temp
            
        return house2


     
