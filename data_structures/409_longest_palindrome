## https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ## still slow !!
        ans = 0
        for v in Counter(s).values():
            ans += (v//2) *2
            if ans%2 == 0 and v%2 == 1:
                ans += 1
        return int(ans)
        
        ## My solution: requires 2 for loops
        # sCount = Counter(s)
        # evenCount = [2*(i//2) for i in list(sCount.values())]
        # oddCount = [i%2 for i in list(sCount.values())]
        # print(evenCount, oddCount)
        # oddLen = 1 if 1 in oddCount else 0
        # return sum(evenCount) + oddLen
