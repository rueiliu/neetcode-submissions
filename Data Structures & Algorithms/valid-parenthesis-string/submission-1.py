'''
create cmin and cmax (the max/min amount of left parenthesis)

if meet ( all +1, if ) all -1, if * cmin-1 cmax +1

if cmax <0 then false

cmin always >= 0 because u can always utilize * to become (

if all ) cmax < 0 will be in effect first

check if cmin ==0




'''

class Solution:
    def checkValidString(self, s: str) -> bool:

        cmax, cmin = 0, 0

        for c in s:
            if c == "(":
                cmax += 1
                cmin += 1
            elif c == ")":
                cmax -= 1
                cmin -= 1
            else:
                cmax += 1
                cmin -= 1
            if cmax < 0:
                return False

            cmin = max(cmin, 0)

       

        return cmin == 0
        