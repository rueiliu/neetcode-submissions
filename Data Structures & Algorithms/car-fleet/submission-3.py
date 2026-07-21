'''

calculate the dest arrival time of the car, and sort with descending order(position wise)

then apply stack to compare the time, if car after arrival time < car before arrival time->fleet(pop)

return len(stack)



'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = sorted(zip(position, speed), reverse = True)
        stack = []
        #create the whole stack list of each car arrival time
        for p, s in time:
            stack.append((target-p)/s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
      

        return len(stack) 
            


        