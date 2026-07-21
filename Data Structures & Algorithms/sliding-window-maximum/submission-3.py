'''
sliding window and monotonic deque, deque is used to store index
while right pointer hasn't reached the right edge:

    test if the current minimum is smaller than new numer(if it does then pop)
    and add new number

    test if left window slips out

    if length fits, append to output and move the pointer




'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l, r = 0, 0       

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res   