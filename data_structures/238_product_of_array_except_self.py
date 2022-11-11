## https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = reduce(lambda a, b: a*(b if b else 1), nums, 1)
        print(prod)
        zero_cnt = nums.count(0)
        if zero_cnt > 1: 
            return [0]*len(nums)
        
        for i, c in enumerate(nums):
            if zero_cnt: 
                nums[i] = 0 if c else prod
            else: 
                nums[i] = prod // c
        return nums
        
        
        ## My solution after few trials
        ## Time complexity = O(N), space complexity = O(N)??
#         ans = []
#         zeroInList = False
#         product = 1
#         for val in nums:
#             if val==0:
#                 if zeroInList == True:
#                     product = 0
#                 else:
#                     product = product
#                 zeroInList = True
#             else:
#                 product *= val
        
#         for i, val in enumerate(nums):
#             if zeroInList and val !=0:
#                 ans.append(0)
#             if zeroInList and val == 0:
#                 ans.append(product)
#             elif zeroInList == False:
#                 ans.append(product//val)
#         return ans
