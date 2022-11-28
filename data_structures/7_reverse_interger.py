## https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        ## Somebody's solution
        s = str(abs(x)) 
        revers = int(s[::-1])
        if revers > 2147483647:
            return 0
        return revers if x > 0 else (revers * -1)
        
        
        ## My solution
#         list_x = list(str(x))
        
#         if list_x[0]=="-":
#             print(list_x, list_x[0], list_x[::-1][:-1])
#             new_list_x = [list_x[0]] + list_x[::-1][:-1]
#         else:
#             new_list_x = list_x[::-1]
#         print(new_list_x)
#         new_val = int(''.join(new_list_x))
#         return new_val if -(2**31)<=new_val<=(2**31)-1 else 0
