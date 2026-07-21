'''
stack/list for index/result list

iterate through temperatures with for loop
check if temp is higher than stack[-1]
if higher than pop and put the new temp
result store the day difference

use index to track temp



'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res