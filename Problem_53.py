class Solution:
    def maxSubArray(self,nums:[list[int]]) -> int:
        res = nums[0]
        maxEnding = nums[0]
        for index in range(1,len(nums)):
            maxEnding = max(nums[index], maxEnding + nums[index])
            res = max(res,maxEnding)

        return res

solution = Solution()

array = [-2,1,-3,4,-1,2,1,-5,4]

print(solution.maxSubArray(array))