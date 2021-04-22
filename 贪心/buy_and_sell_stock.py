"""
[7,1,5,3,6,4]

是否当天出售

"""
nums = [7, 1, 5, 3, 6, 4]


def sell_and_buy(nums):
    res = 0
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            res += nums[i] - nums[i - 1]
    return res


print(sell_and_buy(nums))
