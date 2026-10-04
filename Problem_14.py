class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        longestPrefix = strs[0]
        for string in strs[1:]:
           while not string.startswith(longestPrefix):
               longestPrefix = longestPrefix[:-1]

               if longestPrefix == "":
                   return ""
               

        return longestPrefix

solution = Solution()
array = ["flower", "flow", "flight"]

print(solution.longestCommonPrefix(array))