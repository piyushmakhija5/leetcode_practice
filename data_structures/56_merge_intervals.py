## https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## another sort and merge solution: O(N Log N)
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        
        ## sort and merge: O(N logN)
#         intervals.sort(key=lambda x: x[0])
        
#         check = 0
#         while check < len(intervals)-1:
#             cur = intervals[check]
#             nxt = intervals[check+1]
#             if nxt[0] <= cur[1] and nxt[0]>=cur[0]:
#                 cur[1] = max(nxt[1],cur[1])
#                 intervals.pop(check+1)
#             else:
#                 check += 1
#         return intervals
            
