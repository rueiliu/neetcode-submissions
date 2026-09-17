class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n !=1 and n not in seen:
            seen.add(n)
            n = self.sumofsquare(n)
            

        if n == 1:
            return True

        return False




    def sumofsquare(self, n: int) -> int:
        output = 0

        while n:
            # get the last digit of the integer
            digit = n % 10
            digit = digit * digit
            output += digit
            n = n // 10

        return output
        