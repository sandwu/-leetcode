

matrix = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]


class Solution:
    def search(self, matrix, target):
        row, columns = 0, len(matrix[0]) - 1
        while row < len(matrix) and columns >= 0:
            tmp = matrix[row][columns]
            if target == tmp:
                return True
            elif target > tmp:
                row += 1
            else:
                columns -= 1
        return False


s = Solution()
print(s.search(matrix, 12))
print(12 in matrix)
