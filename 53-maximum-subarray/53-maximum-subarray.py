class Solution(object):
    def maxSubArray(self, nums):
        cs=0
        maxS=-999999
        for nums in nums:
            cs+=nums
            if cs>maxS:
                maxS=cs
            if cs<0:
                cs=0
        return maxS
        
        