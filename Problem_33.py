class Solution:
    def search(self,nums:list[int],target:int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                ##partea stanga este sortata
                if nums[left] <= target < nums[mid]:
                    ##se afla in partea sortata (stanga)
                    right = mid - 1
                else:
                    ##se afla in partea nesortata
                    left = mid + 1
            else:
                ##partea din dreapta este sortata
                if nums[mid] < target <= nums[right]:
                    ##se afla in partea dreapta(sortata)
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

solution = Solution()
array = [4,5,6,7,0,1,2]
target = 0
print(solution.search(array,target))