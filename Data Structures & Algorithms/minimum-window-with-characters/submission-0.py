'''
use hash map and sliding window to check if the substring exists
create one hashmap called count_t, with count_t storing the frequency of str t 
create another hashmap called windows that store the frequency of str s
set up two variables called have and need, need is the len of t, while have is to evaluate if t is in
s based on the frequencies of each character








'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        # hashmap for elements in t
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT) # always unique
        res, resLen = [-1,-1], float("infinity")
        l = 0
        # try to scan through s
        for r in range(len(s)):
            
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # add new elements into the hashmap
            if c in countT and window[c] == countT[c]:
                have += 1


            #try to see if can shorten
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l : r+1] if resLen != float("infinity") else ""



            

        