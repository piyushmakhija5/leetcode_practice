## https://leetcode.com/problems/divisor-game/description/

class Solution:
    def divisorGame(self, n: int) -> bool:
        ## Odd number has odd factors
        return n%2==0
        
