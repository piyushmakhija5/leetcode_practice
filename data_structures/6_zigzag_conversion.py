## https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ## Concise and confusiong solution
        m, li = ['']*numRows, list(range(numRows)) + list(range(numRows-2, 0, -1))
        for ind, ch in enumerate(s):
            m[li[ind % (numRows*2-2) if not numRows*2-2 == 0 else 0]] += ch
        return "".join(m)        
        
        ## Recommended Soltuion
        # if numRows == 1:
        #     return s
        
        # numCols = ceil(len(s)/(2*numRows-2)) * (numRows-1)

        # mat = [['' for r in range(numCols)] for c in range(numRows)]

        # cur_row, cur_col = 0, 0
        # cur_string_idx = 0

        # while cur_string_idx < len(s):
        #     while (cur_row < numRows) and (cur_string_idx < len(s)):
        #         mat[cur_row][cur_col] = s[cur_string_idx]
        #         cur_row += 1
        #         cur_string_idx += 1
            
        #     cur_row -= 2
        #     cur_col += 1
        
        #     while cur_row > 0 and cur_col < numCols and cur_string_idx < len(s):
        #         mat[cur_row][cur_col] = s[cur_string_idx]
        #         cur_row -= 1
        #         cur_col += 1
        #         cur_string_idx += 1
            
        #     ans = ""
        #     for row in mat:
        #         ans += "".join(row)
            
        # return ans
