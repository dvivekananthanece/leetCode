class Solution:  
  def removeDuplicates(nums: list[int]) -> int: 
    final_list = list(*set(nums))
    test = len(final_list)
    length = len(nums)-test
    for i in range(length):
      final_list.append(' ')
    return (list(test).append(final_list))
  print(removeDuplicates([0,0,8,1,1,2,2,3,3,4]))