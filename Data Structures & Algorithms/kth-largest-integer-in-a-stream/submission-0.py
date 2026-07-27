'''
utilize heap structure
bc [0] always minimum, so a heap with k element means [0] is the kth largest


'''


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        #remove > k elements

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


        return self.minHeap[0]
        
