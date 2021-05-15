

class Solution:
    def finduniquenum(self, nums):
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        return False



nums = [0, 1, 2, 3, 2, 5, 3]

s = Solution()
print(s.finduniquenum(nums))
