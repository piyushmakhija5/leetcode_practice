# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        return (counter1 == counter2)
        # return ((not counter1 - counter2)
        #     and (not counter2 - counter1))