## https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## O(log(M+N)) solution 
        # a, b = sorted((nums1, nums2), key=len)
        a = nums1
        b = nums2
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            print(lo,hi,i, after)

            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
        
        ## O(M+N) solution
        # nums3 = []
        # l = r = 0
        # while l<len(nums1) or r<len(nums2):
        #     # print(l,r,nums3)
        #     if l==len(nums1) and r<len(nums2):
        #         nums3.append(nums2[r])
        #         r+=1
        #     elif l<len(nums1) and r==len(nums2):
        #         nums3.append(nums1[l])
        #         l += 1
        #     elif nums1[l]<=nums2[r]:
        #         nums3.append(nums1[l])
        #         l +=1
        #     elif nums1[l] > nums2[r]:
        #         nums3.append(nums2[r])
        #         r += 1
        # return median(nums3)
