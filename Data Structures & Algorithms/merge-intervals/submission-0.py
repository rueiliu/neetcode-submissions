'''
first sort the intervals(using the first number)
create a list called output, put the first sorted list in it

for loop that compares the lastest list(second number), if larger than the current loop first num, then there's a overlap
then merge the two lists
otherwise just append the list
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i:i[0])
        output =[intervals[0]]

        for start, end in intervals[1:]:
            LastEnd = output[-1][1]

            if start <= LastEnd:
                output[-1][1] = max(LastEnd, end)
            else:
                output.append([start, end])

        return output
        