## https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = [nums[0]]
        curMax = [nums[0]]
        for i in range(1, len(nums)):
            curMin.append(min(nums[i], curMin[i-1]*nums[i], curMax[i-1]*nums[i]))
            curMax.append(max(nums[i], curMin[i-1]*nums[i], curMax[i-1]*nums[i]))
        print(curMin, curMax)
        return max(curMax)

        ## Simple O(N)^2 solution: Time limit Exceeded
        # if not nums:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]
        
        # maxProd = -2**31
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         cur = functools.reduce(lambda a, b: a*b, nums[i:j])
        #         # print(i,j, cur)
        #         if cur > maxProd:
        #             maxProd = cur
        # return maxProd
