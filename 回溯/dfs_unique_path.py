

"""
m = 3, n=2

output: 3
只能向下或者向右，网格移动，所以三种：右右下，右下右，下右右

"""


class Solution:
    def unique_path(self, m, n):
        res = self.dfs(0, 0, m-1, n-1)
        return res

    def dfs(self, i, j, m, n):
        if i == m and j == n:
            return 1
        if i > m or j > n: return 0
        res = self.dfs(i+1,j,m,n) + self.dfs(i, j+1, m, n)
        return res

s = Solution()
print(s.unique_path(3, 2))
