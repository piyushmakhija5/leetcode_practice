# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    ## Slightly faster solution: O(N)
    def firstUniqChar(self, s: str) -> int:
        sCount = Counter(s)
        # print(sCount)
        for i, char in enumerate(s):
            if sCount[char] == 1:
                return i
        return -1
    
    ## Building our own counter here: O(N)
#     def firstUniqChar(self, s: str) -> int:
#         counter = {}
#         for letter in s:
#             # print(letter)
#             if letter in counter:
#                 counter[letter] += 1
#             else:
#                 counter[letter] = 1
#         for key, val in counter.items():
#             # print(key, val)
#             if val == 1:
#                 return s.find(key)
#         return -1
