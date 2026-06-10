class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
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
        '''

        l, r = 0, len(s) - 1 

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l, r = l+1, r-1

        return True


# solution with space complexity O(1)

    def alphanum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9') 
        )


            