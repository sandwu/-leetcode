

"""
nums = [1, 2, 3]
output:
[1]
[2]
[3]
[1,2]
[1.3]
[2,3]
[1,2,3]
[]

"""

nums = [1, 2, 3]


class Solution:
    def subsets(self, nums):
        self.res = []
        self.dfs(0, [], nums)
        return self.res

    def dfs(self, index, path, nums):
        self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(i+1, path+[nums[i]], nums)


s = Solution()
print(s.subsets(nums))


"""
nums = [1, 2, 2]
output:
[1]
[1, 2]
[2]
[1, 2, 2]
[]
[2, 2]

nums可重复，output不可重复
"""
nums = [1, 2, 2]

class Solution:
    def subsets(self, nums):
        nums.sort()
        self.res = []
        self.dfs(0, [], nums)
        return self.res

    def dfs(self, index, path, nums):
        self.res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(i+1, path+[nums[i]], nums)


s = Solution()
print(s.subsets(nums))
