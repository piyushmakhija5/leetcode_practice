## https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for others in strs:
                if others[i]!=ch:
                    return shortest[:i]
        return shortest
