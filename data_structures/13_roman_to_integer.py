## https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
                
        val = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            val += conv[char]
        return val
        
        
        ## First solution -- lot of coding effort
#         conv = {"I": 1,
#                 "V": 5,
#                 "X": 10,
#                 "L": 50,
#                 "C": 100,
#                 "D": 500,
#                 "M": 1000}
        
#         val = 0
#         for i, ch in enumerate(s):
#             if ch=='C' and i<len(s)-1 and s[i+1] in ('D','M'):
#                 val -= 100
#             elif ch=='X' and i<len(s)-1 and s[i+1] in ('L','C'):
#                 val -= 10
#             elif ch=='I' and i<len(s)-1 and s[i+1] in ('V','X'):
#                 val -= 1
#             else: 
#                 val += conv[ch]
#         return val
