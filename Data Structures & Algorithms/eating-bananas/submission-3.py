'''
binary search - search from 1 to max(piles) and return minimum hour



'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles) #anything above max(piles) doesn't matter


        while l <= r:
            k = (l + r) // 2
            totaltime = 0

            for pile in piles:
                totaltime += math.ceil(pile/k)

            if totaltime <= h:
                res = k
                #res = min(res, k)
                r = k - 1
            else:
                l = k + 1


        return res


      


        