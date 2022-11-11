## https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         count = sums = 0
#         d = defaultdict(int)
#         d[0] = 1

#         for n in nums:
#             sums += n
#             count += d[sums-k]
#             d[sums] += 1
#         return count
    
    
    ## Old solution
        ans = 0
        cur_sum = 0
        
        seen = collections.defaultdict(int)
        seen[0] = 1
        n = len(nums)
        
        for j in range(n):
            cur_sum += nums[j]
            target = cur_sum-k
            
            ans+=seen[target]
            seen[cur_sum]+=1
            
        return ans
