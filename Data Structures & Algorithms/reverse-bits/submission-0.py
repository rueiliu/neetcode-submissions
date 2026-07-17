'''
use the property of and(&)/or(|)
when 0&1 -> 0, 1&1 -> 1, 0&0->0; 0|1->1, 1|1 ->1, 0|0->0

first extract the end bit from the bits with using & 1
then push it to the front by using | res(the reason to use res here is bc numeber should be big, so res=000000)


'''

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res
        