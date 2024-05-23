class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums =sorted(nums1+nums2)
        i = len(nums)
        if i%2 == 1:
            return nums[i//2]
        else:
            a = (nums[i//2] + nums[(i//2)-1])
            return float(a *0.5)