## https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j), (i,c), (i//3,j//3,c)]
        return len(seen) == len(set(seen))
    
## Classic way
# class Solution:
#     def validateList(self, inputList):
#         filterList = [val for val in inputList if val != '.']
#         return True if len(set(filterList)) == len(filterList) else False
    
#     def validateRow(self, board):
#         for row in board:
#             if self.validateList(row) == False:
#                 print("Row Epic fail", row)
#                 return False
#         return True
    
#     def validateCol(self, board):
#         for i in range(len(board[0])):
#             subList = [item[i] for item in board]
#             if self.validateList(subList) == False:
#                 print("Col Epic fail", subList)
#                 return False
#         return True
    
#     def validateSquare(self, board):
#         for i in range(0, len(board), 3):
#             for j in range(0, len(board[0]), 3):
#                 square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
#                 if self.validateList(square) == False:
#                     print("Square Epic fail", square)
#                     return False
#         return True         
    
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         return (self.validateRow(board) and 
#             self.validateCol(board) and 
#             self.validateSquare(board))