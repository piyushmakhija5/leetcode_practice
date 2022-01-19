## https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n>0:
            if m<=0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else: 
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        if n==0:
            nums1[:n] = nums2[:n]
        
            
        
## Easy Solution  
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:] = nums2[:n]
#         nums1.sort()

## Basic Working Solution
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         num_m = nums1[:m]
#         i , j = 0, 0
#         for x in range(0,m+n):
#             print(x, i, j)
#             if j==n:
#                 nums1[x] = num_m[i]
#                 i+=1
#             elif i==m:
#                 nums1[x] = nums2[j]
#                 j+=1                    
#             elif (i<m) and (j<n) and (num_m[i] <= nums2[j]):
#                 print("cond1")
#                 nums1[x] = num_m[i]
#                 i += 1
#             elif j<n:
#                 print("cond2")
#                 nums1[x] = nums2[j]
#                 j += 1
#         print(nums1)