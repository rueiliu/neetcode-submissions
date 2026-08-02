'''

apply heap, turn nums into negative to create minheap
after heap is created, creata a varibale to track kth



'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        track = 0

        while track < k:

            res = heapq.heappop(nums)
            track += 1

        return -res



        