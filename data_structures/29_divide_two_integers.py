## https://leetcode.com/problems/divide-two-integers/description/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int: 
        if divisor == 0:
            return None

        neg = ((dividend <0) != (divisor <0))
        divid = abs(dividend)
        divis = abs(divisor)
        quo = len(range(0,divid-divis+1,divis))
        if neg:
            quo = -quo
        
        minus_limit = -2**31
        plus_limit = 2**31-1
        quo = min(max(quo,minus_limit), plus_limit)
        return quo
