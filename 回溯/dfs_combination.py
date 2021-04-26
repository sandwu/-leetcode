
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


"""
nums = [10, 1, 2, 7, 6, 1, 5]
target = 8
output:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

nums包含重复，output不能包含重复使用
"""
nums = [10, 1, 2, 7, 6, 1, 5]
target = 8


class Solution2():
    def combination(self, nums, target):
        nums.sort()
        self.res = []
        self.dfs([], 0, nums, target)
        return self.res

    def dfs(self, path, index, nums, target):
        if target < 0: return
        if target == 0:
            self.res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(path+[nums[i]], i+1, nums, target-nums[i])


a = Solution2()
print(a.combination(nums, target))


"""
给定任意k个数，寻找和为target 的集合:不能重复使用数字
给定的数只能是0-9的
k=3, target=7
outpu:
[1, 2, 4]
"""
k = 3
target = 7

class Solution3:
    def combination(self, k, target):
        self.res = []
        self.dfs([], k, target, 1)
        return self.res

    def dfs(self, path, k, target, index):
        if k < 0 or target < 0: return
        if k==0 and target == 0:
            self.res.append(path)
            return
        for i in range(index, 10):
            self.dfs(path+[i], k-1, target-i, i+1)


a = Solution3()
print(a.combination(3, 21))
