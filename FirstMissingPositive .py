class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sortedArray = sorted(list(filter(lambda x: x > 0, [*set(nums)])))
        sortedArray.append(0)
        print(sortedArray)
        for i in range(0, len(sortedArray)):
            print(sortedArray[i],i)
            if sortedArray[i] != i+1:
                return i+1



    print(firstMissingPositive([1,2,0]))
