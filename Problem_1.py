class Solution:
    def twosum(self,nums:list[int],target:int) ->list[int]:
        result = []

        HashSet = {}

        for index,num in enumerate(nums):
            
            if target - num in HashSet:
                result.append(HashSet[target - num])
                result.append(index)
            HashSet[num] = index

        return result

solution = Solution()
array = [2,7,11,15]
target = 9
print(solution.twosum(array,target))