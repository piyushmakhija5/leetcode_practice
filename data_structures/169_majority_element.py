## https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Using sorting: O(nlgn) time complexity, O(1) or O(N) space complexity depending on whether in place sorting is allowed
        nums.sort()
        return nums[len(nums)//2]
        
        ## Using counter: O(N) time complexity, O(N) space complexity
#         nCount = Counter(nums)
#         for i in nCount:
#             if nCount[i] >= len(nums)/2:
#                 return i
        
#         ## Using mode function
#         return mode(nums)
