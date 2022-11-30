## https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l = 0
        r = len(nums)
        while l<r:
            m = (l+r)//2
            
            if (nums[m] < nums[0]) == (target < nums[0]):
                mid = nums[m]
            elif target < nums[0]:
                mid = float('-inf')
            else:
                mid = float('inf')
                
            if mid < target:
                l = m+1
            elif mid > target:
                r = m
            else:
                return m
        return -1
