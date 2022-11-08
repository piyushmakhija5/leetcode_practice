## https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        
        m0 = nums.count(0)
        m1 = m0 + nums.count(1)
        m2 = m1 + nums.count(2)
        
        for i in range(len(nums)):
            if i < m0:
                nums[i] = 0
            elif m0<=i<m1:
                nums[i] = 1
            else:
                nums[i] = 2
        
        
        ## Using python lib sort function --> not allowed
        # nums.sort()
        
