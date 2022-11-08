## https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## set based solution
        return sum(list(set(nums)))*2 - sum(nums)
        
        ## Iterative solution using stack
#         nums.sort()
#         stack = []
#         if len(nums)==1:
#             return nums[0]
#         for i in range(len(nums)):
#             if nums[i] not in stack:
#                 stack.append(nums[i])
#             else:
#                 stack.pop()
#         return stack[0]
        
        ## Using counter
        # nCount = Counter(nums)
        # ans = -inf
        # for n in nCount:
        #     if nCount[n]==1:
        #         return n
