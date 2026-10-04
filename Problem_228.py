class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if nums == []:
            return []
        
        startingNumber = nums[0]
        for index in range(len(nums) - 1):
            if nums[index + 1] - nums[index] != 1:
                endingNumber = nums[index]

                if startingNumber == endingNumber:
                    result.append(str(startingNumber))
                else:
                    result.append(f"{startingNumber}->{endingNumber}")

                startingNumber = nums[index + 1]

        endingNumber = nums[-1]
        if startingNumber == endingNumber:
            result.append(str(startingNumber))
        else:
            result.append(f"{startingNumber}->{endingNumber}")
       
        return result

solution = Solution()
array = [0,1,2,4,5,7]
print(solution.summaryRanges(array))