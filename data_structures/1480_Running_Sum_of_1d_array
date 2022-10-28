## https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(self, nums: List[int]) -> List[int]:
        ## Slightly optimized O(N) solution
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
    
        # ## Basic Solution: O(N)
        # curSum = 0
        # runSumList = []
        # for i in nums:
        #     curSum = curSum + i
        #     runSumList.append(curSum)
        # return runSumList
