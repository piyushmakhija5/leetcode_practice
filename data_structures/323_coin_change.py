## https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
        return [dp[amount], -1][dp[amount] == MAX]


        # def minCoins(amount, coins, dp):
        #     ans = float('inf')
        #     for i in range(len(coins)):
        #         if amount-coins[i]>=0:
        #             subAns = 0
        #             if dp[amount-coins[i]] != -1:
        #                 subAns = dp[amount-coins[i]]
        #             else:
        #                 minCoins(amount-coins[i], coins, dp)
        #             if subAns != float('inf') and subAns +1 < ans:
        #                 ans = subAns + 1
        #     dp[amount] = ans
        #     return dp[amount]

        # if not amount:
        #     return 0
        # if not coins:
        #     return -1
        # dp = [-1 for _ in range(amount+1)]
        # dp[0] = 0
        # return minCoins(amount, coins, dp)

        
Console
