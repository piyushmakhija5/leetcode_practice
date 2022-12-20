## https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        left = []
        right = []
        newList = []

        for [i,j] in intervals:
            # print(i,j, newInterval)
            if (j < newInterval[0]):
                ## no overlap + no insert required
                left.append([i,j])
            elif (i > newInterval[1]):
                ## no overlap but insert should happend before this interval
                right.append([i,j])
            else:
                if (j > newInterval[1]):
                    newInterval[1] = j
                if (i < newInterval[0]):
                    newInterval[0] = i
        newList.append(newInterval)
        return left + newList + right
