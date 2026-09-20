'''
0. check edge case, if either is 0 then return 0
1. m = len(num1), n = len(num2), create an array [0] * (m+n) (longest)
2. two for loops that  calculate the product, use ACSII(-ord(0))
3. the digit place would be i+j+1, the digit one place forward would be i+j
4. add exisiting value of array to i+j+1, then for i+j+1 % 10, i+j // 10
5. remove the 0 ahead(if there's any)
6. return the string by using join


'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        res = [0] * (m+n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p1, p2 = i+j, i+j+1


                #calculate digits
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10

        #remove starting 0
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        return "".join(map(str, res[start:]))
                    