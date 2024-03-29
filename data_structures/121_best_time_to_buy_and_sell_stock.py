# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minBuy = 0, inf
        for price in prices:
            # print("incoming: ", minBuy, maxP, price)
            minBuy = min(minBuy, price)
            maxP = max(maxP, price-minBuy)
            # print("Outgoing: ", minBuy, maxP, price)
        return maxP

## Time limit exceeded   
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxP = 0
#         for i in range(len(prices)):
#             for j in range(len(prices)):
#                 if i<j:
#                     maxP = max(maxP, (prices[j]-prices[i]))
#         return maxP
