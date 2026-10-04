class Solution:
    def threeSum(self,nums:list[int]) -> list[list[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1
            while(left < right):
                if nums[index] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[index] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    new_set = [nums[index],nums[left],nums[right]]
                    result.append(new_set)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1                


        return result   

solution = Solution()
array = [-1,0,1,2,-1,-4]

print(solution.threeSum(array))