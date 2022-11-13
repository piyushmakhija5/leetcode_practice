## https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        table = dict()
        if (len(pattern) != len(words)) or (len(set(pattern)) != len(set(words))):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in table:
                table[pattern[i]] = words[i]
            elif table[pattern[i]] != words[i]:
                return False
        return True
        
        
        ## Non Hashtable solution
#         sSplit = s.split()
#         if len(pattern)!= len(sSplit):
#             # print("length mismatch")
#             return False
        
#         for i in range(len(pattern)):
#             print(pattern[i], pattern.find(pattern[i]), sSplit[i], sSplit.index(sSplit[i]))
#             if pattern.find(pattern[i]) != sSplit.index(sSplit[i]):
#                 return False
#         return True
