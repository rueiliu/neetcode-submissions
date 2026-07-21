'''
use stack to store data
whenever ecounter operators, retrieve the previously 2 elements in stack

'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            res = []
            operator =["+", "-", "*", "/"]
            result = 0

            for word in tokens:
                if word not in operator:
                    res.append(int(word))
                    continue

                if word in operator:
                    b = res.pop()
                    a = res.pop()
                    


                    if word == "+":
                        result = a + b
                    if word == "-":
                        result = a - b
                    if word == "*":
                        result = a * b
                    if word == "/":
                       result = int(a / b)

                res.append(result)

            return res[-1]


                




        