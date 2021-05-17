

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

    def finduniquenum2(self, nums):
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        return -1

    def finduqiuenumbynotchange(self, nums):
        """
        int l=1,r=nums.size()-1;
        while(l<r){
        int s=0;
        int mid=l+r >>1; //二分划分成区间 [l,mid],[mid+1,r]
        for(auto x:nums) s+= x>=l&&x<=mid;  //求左边的数 个数   总有一边大于n
          if(s>mid-l+1)  {
                r=mid;
          }else l=mid+1;

        }
        return r;
        :param nums:
        :return:
        """
        l = 1
        r = len(nums) - 1
        while l < r:
            mid = (l+r) >> 1
            count_l = 0
            count_r = 0
            for i in nums:
                if l <= i <= mid:
                    count_l += 1
                else:
                    count_r += 1
            if count_l > mid - l + 1:
                r = mid
            else:
                l = mid + 1
        return l

nums = [0, 1, 2, 3, 2, 5, 3]

s = Solution()
print(s.finduniquenum(nums))

num2 = [2, 3, 5, 4, 6, 2, 6, 7]
print(s.finduqiuenumbynotchange(num2))
