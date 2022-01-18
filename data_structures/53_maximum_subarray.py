## https://leetcode.com/problems/maximum-subarray/

## Another DP Solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        # print(dp)
        return max(dp)

## DP Solution   
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0] = dp[1][0] = nums[0]
        for i in range(1,len(nums)):
            dp[1][i] = max(nums[i], nums[i]+dp[1][i-1])
            dp[0][i] = max(dp[1][i], dp[0][i-1])
        # print(dp)
        return dp[0][-1]

## Pythonic Solution --> No DP --> O(N)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = nums[0]
#         curSum = nums[0]
#         for i in range(1,len(nums)):
#             curSum = max(nums[i], curSum+nums[i])
#             # print(i,curSum,maxSum)
#             maxSum = max(maxSum, curSum)
#         return maxSum
    
        
## Brute Force --> O(N^2)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = -inf
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i,len(nums)):
#                 total += nums[j]
#                 maxSum = max(total, maxSum)
#         return maxSum
