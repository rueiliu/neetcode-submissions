'''
I have a string s that consists of a series of 
characters

I need to verify if string s is valid(return true or false)

conditions:
1.same type characters
2.{}[]()


1.check if the length is the same, if not, return False
2.left side will only be ([{
3.use location to check if there are corresponding brackets

1. if else statement
2. for loop that iterates half of the length and check if all are left side brackets
3. in the same for loop, check the if corresponding charater is a match 


'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedict = {')':'(', '}':'{', ']':'['}

        for i in s:
            if i in closedict:
                if stack and stack[-1] == closedict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)


        if len(stack) > 0:
            return False
        else:
            return True

        