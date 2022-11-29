## https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ## Hashmap approach
        count = Counter(words)
        ans = 0
        center = False
        for word, cnt_word in count.items():
            if word[0]==word[1]:
                if cnt_word %2 == 0:
                    ans += cnt_word
                else:
                    ans += cnt_word-1
                    center = True
            elif word[0]<word[1]:
                ans += 2* min(cnt_word, count[word[1]+word[0]])
        if center:
            ans += 1
        return 2*ans
        
        
        ## word and its reverse needs to be present is the words list
        ## unless, the word is reverse of itself --> only 1 of those can be used
        ## abandoned approach --> yet to check if we have 2 indexes with "gg" kind of word
#         forward = []
#         back = []
#         center = []
#         seen = set()
#         for i in range(len(words)):
#             if words[i][::-1] in words and words[i] not in seen:
#                 if words[i] == words[i][::-1] :
#                     if not center:
#                         center.append(words[i])
#                         seen.add(words[i])
#                     else:
#                         continue
#                 else:
#                     forward.append(words[i])
#                     back.append(words[i][::-1])
#                     seen.add(words[i])
#                     seen.add(words[i][::-1])
        
#         return len((''.join(forward)) +''.join(center) + ''.join(back[::-1]))
