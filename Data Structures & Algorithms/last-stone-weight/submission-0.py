'''
U: input list, output list, edge case-> len(stones) == 0
M: heap
P: first turn the heap into negative ones(bc pythong only has minheap, then use while loop to calculate the first two smallest value(pop) until ending condition is reached



'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-num for num in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            #retrieve the first and second stone

            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        
        return abs(stones[0]) if stones else 0

        