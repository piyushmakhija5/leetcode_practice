## https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_map = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        r1 = 0
        r2 = 0
        for i in num1:
            r1 = 10*r1 + num_map[i]
        for j in num2:
            r2 = 10*r2 + num_map[j]
        return (str(r1*r2))

        
        ## not allowed
        # return str(int(num1)*int(num2))
