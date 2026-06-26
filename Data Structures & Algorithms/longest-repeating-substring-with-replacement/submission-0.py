'''
Use sliding window 
store occurence in dict
in every iteration, expand the right side but check if the amt of different uppercase has exceed k
if exceede, move the left side until = k






'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        l = 0
        length = 0
        remain_sum = 0
        for i in range(len(s)):
            char[s[i]] = char.get(s[i], 0) + 1
            max_char = max(char.values()) if char else 0
            remain_sum = sum(char.values()) - max_char
            while remain_sum > k:
                char[s[l]] -= 1
                l += 1
                max_char = max(char.values()) if char else 0
                remain_sum = sum(char.values()) - max_char
            
            length = max(length, i-l+1)

        return length
