## https://leetcode.com/problems/find-pivot-index/

def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        l = 0
        for i,x in enumerate(nums):
            if l == S - l - x:
                return i
            l += x
        return -1
        
        ## Taking too long
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1
