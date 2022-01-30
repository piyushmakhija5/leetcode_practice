# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # print("\n",ransomNote, magazine)
        noteCounter = collections.Counter(ransomNote)
        magCounter = collections.Counter(magazine)
        # print(noteCounter, magCounter)
        return not noteCounter - magCounter
    
## Basic Counter based method
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         print("\n",ransomNote, magazine)
#         noteCounter = collections.Counter(ransomNote)
#         magCounter = collections.Counter(magazine)
#         print(noteCounter, magCounter)
#         for key, val in noteCounter.items():
#             print(key, val)
#             if (key in magCounter) and (val<=magCounter[key]):
#                 print("key in magCounter", val, magCounter[key])
#                 pass
#             else:
#                 return False
#         return True