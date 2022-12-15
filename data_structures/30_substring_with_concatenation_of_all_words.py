## https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        n = len(s)
        k = len(words)
        word_count = Counter(words)
        len_word = len(words[0])
        len_substr = k*len_word
        
        def check(i):
            remain = word_count.copy()
            words_used = 0

            for j in range(i, i+len_substr, len_word):
                sub = s[j:j+len_word]
                if remain[sub] > 0:
                    remain[sub] -= 1
                    words_used += 1
                else:
                    break
            return words_used == k

        ans = []
        for i in range(n-len_substr+1):
            if check(i):
                ans.append(i)
        return ans
