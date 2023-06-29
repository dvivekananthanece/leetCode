class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum_number = max(candies)
        returnList = []
        for i in candies:
            if maximum_number <= i+extraCandies:
                returnList.append(True)
            else:
                returnList.append(False)
        return returnList


solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))
