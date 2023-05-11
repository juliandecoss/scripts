
class Solution:
    def twoSum(self, nums:list, target):
        for pos,num in enumerate(nums):
            second = num -target
            if  second + num != target:
                if abs(second) + num == target:
                    second = abs(second)
                elif (-1*second) + num ==target:
                     second = second * -1
            if second in nums and nums.index(second) != pos:
                return [pos, nums.index(second)] 
sol = Solution()
print(sol.twoSum([-1,-2,-3,-4,-5],-8))