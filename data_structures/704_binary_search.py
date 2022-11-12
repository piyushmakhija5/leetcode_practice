## https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r = len(nums)-1
        while (l<=r):
            mid = (r+l)//2
            # print(l,r,mid,nums[mid], target)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
        return -1
