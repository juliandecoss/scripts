
[1,2,3,4]
[24,12,8,6]
from copy import deepcopy
class Solution:
    def productExceptSelf(self, nums:list):
        res = [1] * len(nums)
        prefix = 1 
        postfix = 1
        for i in range(len(nums)) :  # [1,2,6,24]
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1 , - 1 , - 1) :  # [24,24,12,4]
            res[i] *= postfix
            postfix *= nums[i]
        return res
sol = Solution()
a = sol.productExceptSelf([1,2,3,4])
print(a)