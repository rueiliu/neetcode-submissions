'''


use bucket sort algoritm
create a dictionary that has nums as keys, occurences as values
then i will a list that has multiple blank list, each sublist's index refers to the occurences of the nums
given k value, print out sublits's values in descending order

'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        

        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums)+1)]
        #put dict value in bucket

        for key, value in count.items():
            bucket[value].append(key)

        for i in range(len(bucket)-1, 0 , -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


    
            

            