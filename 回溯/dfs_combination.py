
"""
nums = [2, 3, 6, 7]

target = 7

solution = [[7],[2, 2, 3]]

"""

nums = [2, 3, 6, 7]

target = 7

class Solution:
    def combination(self, nums, target):
        self.res = []
        self.dfs([], 0, nums, target)
        return self.res

    def dfs(self, path, index, nums, target):
        if target < 0:return
        if target == 0:self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(path+[nums[i]], i, nums, target-nums[i])

s = Solution()
print(s.combination(nums, target))
