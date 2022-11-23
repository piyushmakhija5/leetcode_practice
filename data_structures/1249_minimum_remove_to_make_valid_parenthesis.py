## https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        new_s = list(s)
        
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            elif ch==')':
                if stack:
                    stack.pop()
                else:
                    new_s[i] = ''
            
        while stack:
            new_s[stack.pop()] = ''
    
        return ''.join(new_s)
