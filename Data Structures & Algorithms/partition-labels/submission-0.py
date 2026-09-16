'''

1. create hashmap to find the ending element loc of letters

2. create a empty list(res) to store results, 
and size(current count size) and current end to record current index.
use a for loop to compare current end

3. if current end has reached the ending of specific element in the hashmap, append size to res and reset size to 0



'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = {}

        # store last location
        for i, c in enumerate(s):
            res[c] = i

        #
        result = []
        size, end = 0, 0

        for i in range(len(s)):
            size += 1
            end = max(end, res[s[i]])

            if i == end:
                result.append(size)
                size = 0

        return result



        