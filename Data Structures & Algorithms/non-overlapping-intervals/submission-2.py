'''
first sort
and compare if there's overlapping
every removal += 1





'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        prevend = intervals[0][1]
        remove = 0

        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                remove += 1
                prevend = min(prevend, end)

        

        return remove


        