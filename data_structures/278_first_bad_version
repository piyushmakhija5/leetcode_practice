## https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        low = r
        while l<=r:
            mid = (l+r)//2
            # print(l,r,mid)
            if isBadVersion(mid):
                low = min(low,mid)
                r = mid-1
            else:
                l = mid+1
        return low
