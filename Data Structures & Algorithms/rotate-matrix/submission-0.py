'''
use two pointer to iterate every side of the matrix




'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1

        while l < r: # there might be multiple layers
            top = l
            bottom = r
            for i in range(r-l): # ignore the last one otherwise it'd be rotate twice
                # save the top row first
                topLeft = matrix[top][l+i]
                # move left column into top column
                matrix[top][l+i] = matrix[bottom-i][l]

                #move bottom row to left column
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #move right column to bottom row
                matrix[bottom][r-i] = matrix[top+i][r]

                #move top row to right column
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1

        