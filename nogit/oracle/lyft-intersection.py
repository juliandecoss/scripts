nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1 = [1,4,5,3,6]
nums2 = [2,3,5,7,9]
class Solution:

    @staticmethod
    def intersection(nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]
            
print(Solution.intersection(nums1,nums2))