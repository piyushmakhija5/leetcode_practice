## https://leetcode.com/problems/contains-duplicate/

# Using Python Set Function
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
            
    
# Using Counter dict/hashmap approach
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         counter = {}
#         for num in nums:
#             if num not in counter:
#                 counter[num] = 0
#             counter[num] += 1
#         for num, freq in counter.items():
#             if freq > 1:
#                 return True
#         return False
    
# Sorting approach
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return True
#         return False
    
