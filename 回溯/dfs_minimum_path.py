

"""
Input
path = [
    [1, 3, 1],
    [1, 5, 1],
    [2, 4, 1]
]
output:
7(1->3->1->1->1)
只能向下或者向右
"""

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [2, 4, 1]
]


class Solution:
    def minimum(self, grid):
        self.memo = {}
        m = len(grid)
        n = len(grid[0])
        res = self.dfs(0, 0, m - 1, n - 1, grid)
        return res

    def dfs(self, i, j, m, n, grid):
        if (i, j) in self.memo: return self.memo[i, j]
        if i == m and j == n:
            return grid[i][j]  # 到达右下角，返回对应的值
        d = r = float('inf')
        if i < m:
            d = self.dfs(i + 1, j, m, n, grid)
        if j < n:
            r = self.dfs(i, j + 1, m, n, grid)
        res = min(d, r) + grid[i][j]  # 每个结果都是当前值+向下和向右的最小值
        self.memo[i, j] = res
        return res


s = Solution()
print(s.minimum(grid))
