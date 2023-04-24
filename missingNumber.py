class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sortedArray = sorted(list(filter(lambda x: x >= 0, [*set(nums)])))
        sortedArray.append(0)
        for i in range(0, len(sortedArray)):
            if sortedArray[i] != i:
                return i