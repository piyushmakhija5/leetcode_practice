# https://leetcode.com/problems/intersection-of-two-arrays-ii/

## Double Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (collections.Counter(nums1) & collections.Counter(nums2)).elements()
    
## Using Counter
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         counts = collections.Counter(nums1)
#         res = []
#         for num in nums2:
#             if counts[num]>0:
#                 res.append(num)
#                 counts[num] -= 1
#         return res
    
## Using dict for counter   
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         counts = {}
#         res = []
#         for num in nums1:
#             counts[num] = counts.get(num,0) + 1
#         for num in nums2:
#             if num in counts and counts[num] > 0:
#                 res.append(num)
#                 counts[num] -= 1
#         # print(res)
#         return res