class Solution:
    def productExceptSelf(self,nums : List[int]) -> List[int]:
        result = []
       
        size = len(nums)
        left = [0] * size
        right = [0] * size

        increment = 1
        index = 0
        while True:
            if index == size:
                increment = -1
                index += increment
            #asceding
            if increment == 1:
                if index == 0:
                    left[index] = 1
                else:
                    left[index] = left[index - 1] * nums[index - 1]
                index += increment
            #descedning
            else:
                if index == -1:
                    break
                if index == size - 1:
                    right[index] = 1
                else:
                    right[index] = right[index + 1] * nums[index + 1]
                index += increment

        for index in range(len(nums)):
            result.append(left[index] * right[index])
        return result


solution = Solution()
array = [1,2,3,4]
print(solution.productExceptSelf(array))