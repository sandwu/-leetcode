
"""
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

def twosum(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left+1, right+1]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1


"""
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

nums = [-1, 0, 1, 2, -1, -4]


def threesum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        target = -nums[i]
        left, right = i+1, len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    return res


print(threesum(nums))
