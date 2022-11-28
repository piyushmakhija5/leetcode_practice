## https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        ## Using regex patterns
#         match = re.match(r'^\s*([+|-]?\d+)', string)
        
#         if match:
#             integer = int(match.group())
#             return max(-(1 << 31), min(integer, (1 << 31) - 1))
#         return 0
        
        
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)
        
        ## 1. ignore leading whitespaces
        s = s.strip()
        if s =="":
            return 0
        
        # 2. check for signs
        if s[0] == '-':
            neg = -1
            s = s[1:]
        elif s[0] == '+':
            neg = 1
            s = s[1:]
        else:
            neg = 1
        
        # 3. read next chars until non-digit
        new_s = ''
        for ch in s:
            if ch in digits:
                new_s += ch
            else:
                break
        
        # 4. Convert to integer
        # print(new_s)
        if new_s=='':
            return 0
        res = int(new_s)*neg
        
        # 5. Signed Integer Range
        if res > INT_MAX:
            res = INT_MAX
        elif res < INT_MIN:
            res = INT_MIN

            
        # 6. Return final value
        return res
