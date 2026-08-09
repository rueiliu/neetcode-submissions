'''
backtracking

test if digits is none, if it is return empty list
first create a hashmap of number -> characters
and a empty list res to store result

write a helper function dfs(i, current) for backtracking.
first check if len(current) == leb(digits), if satisfy, then append current into res

then apply a for loop that iterate through the element of digit, then apply bactracking


return res



'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []
        path = []

        chartodigit = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i >= len(digits):
                res.append("".join(path))
                return

            for c in chartodigit[digits[i]]:
                path.append(c)
                dfs(i+1)
                path.pop()

        dfs(0)

        return res



        