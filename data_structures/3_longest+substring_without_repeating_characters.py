## https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        pos = defaultdict(int)
        start = 0
        for idx, ch in enumerate(s):
            start = max(start, pos[ch])
            max_len = max(max_len, idx-start+1)
            pos[ch] = idx+1
        return max_len
