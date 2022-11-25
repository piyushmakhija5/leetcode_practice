## https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## O(N) solution: two pointer solution
        maxVal = 0
        i = 0
        j = len(height)-1
        while j>i:
            width = abs(j-i)
            area = width * min(height[i], height[j])
            maxVal = max(maxVal, area)
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
        return maxVal
        
        ## Naive solution: O(N^2)
        # maxVal = -1
        # for idx1,val1 in enumerate(height):
        #     for idx2, val2 in enumerate(height):
        #         if idx1!=idx2:
        #             maxVal = max(maxVal, (min(val1,val2))*(idx2-idx1))
        # return maxVal
