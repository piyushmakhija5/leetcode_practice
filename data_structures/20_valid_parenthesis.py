## https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            elif not stack or mapping[stack[-1]] != ch:
                return False
            else:
                stack.pop()
        return len(stack)==0
        
        ## Basic solution: too many conditions
        # stack = []
        # for input in s:
        #     # print(input, stack)
        #     if input in ['(', '{', '[']:
        #         stack.append(input)
        #     elif input == ')':
        #         if len(stack)==0 or stack[-1] != '(':
        #             return False
        #         stack.pop()
        #     elif input == '}':
        #         if len(stack)==0 or stack[-1] != '{':
        #             return False
        #         stack.pop()
        #     elif input == ']':
        #         if len(stack)==0 or stack[-1] != '[':
        #             return False
        #         stack.pop()
        # return True if len(stack)==0 else False
