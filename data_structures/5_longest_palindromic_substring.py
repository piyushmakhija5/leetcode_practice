## https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # m=''
        # for i in range(len(s)):
        #     for j in range(lens,i,-1):
        #         if len(m) > j=i:
        #             break
        #         elif s[i:j]==s[i:j][::-1]:
        #             m = s[i:j]
        #             break
        # return m
        
        ## Expand around center approach
        self.maxlen = 0
        self.start = 0
        for i in range(len(s)):
            self.expandFromCenter(s,i,i)
            self.expandFromCenter(s,i,i+1)
        return s[self.start:self.start+self.maxlen]
    
    def expandFromCenter(self,s,l,r):
        while l>-1 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l+1
        
        ## O(N)^2 time solution with O(n)^2 space complexity
#         ans = ''
#         dp = [[0]*len(s) for _ in range(len(s))]
#         for i in range(len(s)):
#             dp[i][i] = True
#             ans = s[i]
            
#         for i in range(len(s)-1, -1, -1):
#             for j in range(i+1, len(s)):
#                 if s[i]==s[j]:
#                     if j-i==1 or dp[i+1][j-1] is True:
#                         dp[i][j] = True
#                         if len(ans) < len(s[i:j+1]):
#                             ans = s[i:j+1]
#         return ans
			
