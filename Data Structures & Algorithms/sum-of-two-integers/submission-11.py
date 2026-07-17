class Solution:
    def getSum(self, a: int, b: int) -> int:

        bitshort = 0xFFFFFFFF
        maxint = 0x7FFFFFFF

        while (b & bitshort) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        a = a & bitshort
        return a if a <= maxint else ~(a^bitshort)

        