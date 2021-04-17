"""
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

nums = [0,1,0,3,12]

def moveZeroes(nums):
    read = write = 0
    while read < len(nums):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
        read += 1
    for i in range(write, read):
        nums[i] = 0
    return nums

print(moveZeroes(nums))


nums = [0,0,1,1,1,2,2,3,3,4]

"""
输出 不重复的数字5
"""

def removeduplicate(nums):
    if not nums: return 0
    read = write = 1
    while read < len(nums):
        if nums[read] != nums[read-1]:
            nums[write] = nums[read]
            write += 1
        read += 1
    return write
