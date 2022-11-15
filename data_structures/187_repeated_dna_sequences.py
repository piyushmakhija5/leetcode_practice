## https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ## Efficient coding of previous solution
        m = {}
        for i in range(len(s)):
            m[s[i : i + 10]] = 1 + m.get(s[i : i + 10], 0)
        return [key for key, value in m.items() if value > 1]
        
        ## Own solution: Time complexity = 2*O(N) = O(N)
        # seqCnt = {}
        # for i in range(0,len(s)):
        #     seq = s[i:i+10]
        #     # print(seq, seqCnt)
        #     if s[i:i+10] not in seqCnt.keys():
        #         seqCnt[seq] = 1
        #     else:
        #         seqCnt[seq] += 1
        # return [i for i in seqCnt if seqCnt[i]>1]
