'''
view the 2-D as an 1D array

Binary Search -> two pointers to find if the value exists



'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        l, r = 0, ROW * COL - 1


        while l <= r:

            mid = (l+r) // 2
            row = mid // COL
            col = mid % COL
            val = matrix[row][col]

            if val == target:
                return True

            elif val < target:
                l = mid + 1

            else:
                r = mid - 1

        return False





        