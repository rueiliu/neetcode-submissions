'''
1.create max/min of 2 to the power of 31
2. slice last digit and the rest(use whie loop to check)
3. check if the rest exceeds the range
4. store the value into a new variable






'''


class Solution:
    
    def reverse(self, x: int) -> int:

        MAX = 2147483647
        MIN = -2147483648   
        res = 0  


        while x:
            digit = int(math.fmod(x, 10))
            x = int (x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (10 * res) + digit

        return res

