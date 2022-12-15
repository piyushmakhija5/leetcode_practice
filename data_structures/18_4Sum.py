## https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums)<4:
            return []

        def kSum(nums, target, k):
            res = []
            if not nums:
                return res
            
            avg_val = target // k
            if (avg_val < nums[0]) or (nums[-1] < avg_val):
                return res

            if k==2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i==0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res


        def twoSum(nums, target):
            res = []
            lo = 0
            hi = len(nums)-1

            while lo < hi:
                curSum = nums[lo] + nums[hi]
                if curSum < target or (lo>0 and nums[lo] == nums[lo-1]):
                    lo += 1
                elif curSum > target or ( (hi < len(nums)-1) and (nums[hi] == nums[hi+1]) ):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
