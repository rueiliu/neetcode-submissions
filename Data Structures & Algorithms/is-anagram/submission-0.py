class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {}
        w1_cnt = 0
        word_2 = {}
        w2_cnt = 0

        if len(s) != len(t):
            return False

        for w1, w2 in zip(s, t):
            if w1 not in word_1:
                word_1[w1] = 1
            word_1[w1] += 1
            if w2 not in word_2:
                word_2[w2] = 1
            word_2[w2] += 1

        for wd in s:
            if wd not in t:
                return False
            elif word_1[wd] != word_2[wd]:
                return False
        
        return True

        
        


        