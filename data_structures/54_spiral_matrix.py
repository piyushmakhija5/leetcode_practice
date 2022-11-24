## https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # One liner solution
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
