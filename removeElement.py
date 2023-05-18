nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
for i in range(0, len(nums) - 1):
    if nums[i] == val:
        del nums[i]
print(len(nums))
