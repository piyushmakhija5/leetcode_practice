## https://leetcode.com/problems/delete-and-earn/description/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        
        N = max(nums)+1
        numCount = [0 for _ in range(N)]
        for num in nums:
            numCount[num] +=1

        dp = [[0,0] for i in range(N)]
        for i in range(1, N):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + i*numCount[i]
        return max(dp[N-1][0], dp[N-1][1])
            
