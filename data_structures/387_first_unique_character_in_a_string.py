# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for letter in s:
            # print(letter)
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
        for key, val in counter.items():
            # print(key, val)
            if val == 1:
                return s.find(key)
        return -1