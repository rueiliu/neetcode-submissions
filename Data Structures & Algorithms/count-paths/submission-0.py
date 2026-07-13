'''
calculate the number of ways from the bottom row and the rightmost column,
use numbers to store the paths for that grid.
rightmost col and bottom row should be 1
apply for loop to move up the calculation to the start

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n


        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2,-1,-1):
                new_row[j] = new_row[j+1] + row[j]
            row = new_row

        return row[0] 


        