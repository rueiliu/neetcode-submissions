'''
This looks like a sliding window problem 
we can use two arrays [0] * 26 to store s1 and s2 and compare if both are the same.

use for loop to slide through the s2 window each time and check if it matches s1

if the for loop ends still no match thenr return False

edge cases: s1=s2, s1>s2



'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        word1 = [0] * 26
        word2 = [0] * 26

        window_size = len(s1)
        # Put data into word1
        for i in range(window_size):
            val1 = ord(s1[i]) - ord("a")
            val2 = ord(s2[i]) - ord("a")
            word1[val1] += 1
            word2[val2] += 1
        if word1 == word2:
            return True

        # Slide through s2 to find a match
        for j in range(window_size, len(s2)):
            val2 = ord(s2[j]) - ord("a")
            val3 = ord(s2[j-window_size]) - ord("a")
            word2[val2] += 1
            word2[val3] -= 1
            if word1 == word2:
                return True

        return False

