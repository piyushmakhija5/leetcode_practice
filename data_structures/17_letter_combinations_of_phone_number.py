## https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tele = {'2': ["a", "b", "c"],
                '3': ["d", "e", "f"],
                '4': ["g", "h", "i"],
                '5': ["j", "k", "l"],
                '6': ["m", "n", "o"],
                '7': ["p", "q", "r", "s"],
                '8': ["t", "u", "v"],
                '9': ["w", "x", "y", "z"]}
        
        if not digits:
            return []
        ans = []
        
        for ch in digits:
            if not ans:
                ans = tele[ch]
            else:
                ans = [x+y for x in ans for y in tele[ch]]
        return ans
