## https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Using sorting
        data = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in data:
                data[sortedWord].append(word)
            else:
                data[sortedWord] = [word]
        return list(data.values())
        
        ## Using 2 dicts and counter: Inefficient code !!
#         if not strs or len(strs)==1:
#             return [strs]
        
#         dataMap = {}
#         resMap = {}
#         for i, s in enumerate(strs):
#             sCnt = Counter(s)
#             if sCnt not in dataMap.values():
#                 dataMap[i] = sCnt
#                 resMap[i] = [s]
#             else:
#                 key = list(dataMap.keys())[list(dataMap.values()).index(sCnt)]
#                 # print(list(mydict.keys())[list(mydict.values()).index(16)]) 
#                 resMap[key].append(s)
#         # print(dataMap, resMap)
#         return list(resMap.values())
