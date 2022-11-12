## https://leetcode.com/problems/isomorphic-strings/

def isIsomorphic(self, s: str, t: str) -> bool:
        ## Clean and one line solution: O(N*2) --> O(N) solution
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
        
        ## Basic solution --> O(N)
        # if (len(s) != len(t)) or (len(set(s)) != len(set(t))):
        #     return False
        # c1 = Counter(s)
        # c2 = Counter(t)
        # hashMap = {}
        # for i,val in enumerate(s):
        #     if val not in hashMap:
        #         hashMap[val] = t[i]
        #     # print(hashMap, hashMap[val], val, t[i])
        #     if (hashMap[val]!=t[i]) or (c1[val] != c2[t[i]]):
        #         return False
        # return True
