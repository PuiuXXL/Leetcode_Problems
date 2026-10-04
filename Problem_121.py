class Solution:
    def maxProfit(self,prices:list[int]) -> int:
        minimum = prices[0]
        maximumProfit = 0
        for price in prices:
            if price < minimum:
                minimum = price
            else:
                profit = price - minimum
                if profit > maximumProfit:
                    maximumProfit = profit

        return maximumProfit


solution = Solution()
array = [7,1,5,3,6,4]
print(solution.maxProfit(array))