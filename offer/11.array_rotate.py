

"""
将有序数组旋转，找到最小的数。
{3,4,5,1,2}  是 {1,2,3,4,5}的旋转

"""


class Solution:

    def rotate_array(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                right = mid + 1
            else:
                right -= 1
        return nums[left]


nums = [1, 2, 3, 4, 5]
s = Solution()
print(s.rotate_array(nums))

