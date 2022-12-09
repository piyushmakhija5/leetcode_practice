## https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
        ret = ""        
        for i, j in enumerate(nums):
            while num >= j:
                ret += strs[i]
                num -= j
            if num == 0:
                return ret


        ## My working Solution
        # roman = ''
        # mapping = {
        #     'M': 1000,
        #     'D': 500,
        #     'C': 100,
        #     'L': 50,
        #     'X': 10,
        #     'V': 5,
        #     'I': 1
        # }

        # for key, value in mapping.items(): 
        #     while num >= value:
        #         roman += key
        #         num -= value

        # print(roman, num)
        # roman = roman.replace('DCCCC', 'CM').replace('CCCC', 'CD')
        # roman = roman.replace('LXXXX', 'XC').replace('XXXX', 'XL')
        # roman = roman.replace('VIIII', 'IX').replace('IIII', 'IV')
        # return roman
