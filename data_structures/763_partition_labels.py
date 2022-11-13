## https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ## leetcode solution
        # last = {c: i for i,c in enumerate(s)}
        # # print(last)
        # j = anchor = 0
        # ans = []
        # for i,c in enumerate(s):
        #     j = max(j,last[c])
        #     if i==j:
        #         ans.append(i-anchor+1)
        #         anchor = i+1
        # return ans
        
        ## Own solution: O(N) --> kind of slow
        res = []
        for i in range(1,len(s)+1):
            # print(i, s[:i], s[i:])
            if not set(s[:i]).intersection(set(s[i:])):
                if not res:
                    res.append(i)
                else:
                    res.append(i-sum(res))
        return res
