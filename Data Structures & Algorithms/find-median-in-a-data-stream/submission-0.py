'''
Use heap, first create small and large heap

push value into small heap(remember first value of small heap is the maximum,
but python does not support that, so we need to times -1)

then check if the properties are all met(small and large exist, and max of small < min of large)
push the val into large(remove the elemnts that pushed into large heap from small heap)


Then move the elements between heaps, first check the length between two heaps
move accordigly

for define median

if len equal, calculate average
if small longer, then first value of small heap
if large longer, then first value of large heap
'''
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and -1 * self.small[0]
        > self.large[0]):

            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        #check the length

        if len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) - len(self.small) > 1:
            val =  heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        

    def findMedian(self) -> float:

        if len(self.small) - len(self.large) == 1:
            return -1 * self.small[0]

        if len(self.large) - len(self.small) == 1:
            return self.large[0]

        if len(self.large) == len(self.small):
            return (-1 * self.small[0] + self.large[0]) / 2
        
        