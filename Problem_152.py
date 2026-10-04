class Solution:
    def maxProduct(self,nums:list[int]) -> int:
        max_product = nums[0]
        max_ending = nums[0]
        min_ending = nums[0]

        for num in nums[1:]:
            old_max = max_ending
            old_min = min_ending

            max_ending = max(
                num,
                old_max * num,
                old_min * num
            )
            min_ending = min(
                num,
                old_max * num,
                old_min * num
            )

            max_product = max(max_ending,max_product)
        
        return max_product

solution = Solution()

array = [2,3,-2,4]
print(solution.maxProduct(array))