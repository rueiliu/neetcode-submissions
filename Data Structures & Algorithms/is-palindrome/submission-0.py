class Solution:
    def isPalindrome(self, s: str) -> bool:
        #decide the amount of checking times
        s2 = ""
        for str in s:    
            if str.isalnum():
                s2 += str.lower()
        time = len(s2) // 2


        for i in range(time):
            if s2[i] != s2[-1-i]:
                return False
        return True 

            