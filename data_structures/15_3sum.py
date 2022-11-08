## https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()
        for i in range(n):
            j = i+1
            k = n-1
            while j<=k:
                s = nums[i] + nums[j] + nums[k]
                if i!=j and i!=k and j!=k and s==0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif s>0:
                    k-=1
                else:
                    j+=1
        return ans
