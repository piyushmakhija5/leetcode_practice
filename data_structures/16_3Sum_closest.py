## https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ## Not able to pass all Test Cases !!
        if not nums or len(nums) < 3 :
            return []
        
        nums.sort() # O(N log N)

        gMin = 1000000
        val = 1000000
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                sum3 = (nums[i] + nums[l] + nums[r])
                # print(i, l, r, sum3, gMin)
                if  abs(target - sum3) < abs(gMin-target):
                    gMin = sum3
                if sum3>target:
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                else:
                    if sum3==target:
                        return target
                    while l<r and nums[l]==nums[l+1]:
                        l += 1
                    l+=1
        return gMin


