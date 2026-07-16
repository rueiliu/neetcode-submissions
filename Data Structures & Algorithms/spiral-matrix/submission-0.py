'''
this is hard,
need to draw the graph
use pointers


'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left < right and top < bottom:

            #record top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            #record right row
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not(left < right and top < bottom):
                break

            #record bottom row, right -1 bc right(exceed border and deducted one just above)
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            #record left row
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


        