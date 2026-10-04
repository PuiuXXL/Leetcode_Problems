class Solution:
    def containsDuplicate(self,nums:list[int]) -> bool:
        HashSet = {}
        for num in nums:
            if num in HashSet:
                return True
            HashSet[num]  = 1
        return False

solution = Solution()
array = [1,2,3,1]
print(solution.containsDuplicate(array))