## https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s=="" or not wordDict:
            return False
        
        ok=[True]
        for i in range(1,len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]
