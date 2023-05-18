from LeetCode import linkedList as ll
from typing import Optional



# ll.linkedList

linkedList = ll.head()
linkedList.head = ll.Node(2)
Node2 = ll.Node(2)
Node3 = ll.Node(4)
Node4 = ll.Node(3)
linkedList.head.next = Node2
Node2.next = Node3
Node3.next = Node4

linkedList2 = ll.head()
linkedList2.head = ll.Node(1)
Node9 = ll.Node(0)
Node8 = ll.Node(1)
linkedList2.head.next = Node9
Node9.next = Node8

class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1= list1.head
        list2 = list2.head
        lists1 = []
        finalList = result = None
        while list1:
            lists1.append(list1.data)
            list1 = list1.next
        while list2:
            lists1.append(list2.data)
            list2 = list2.next
        lists1.sort()
        for i in lists1:
            if finalList is None:
                finalList = result = ListNode(i)
            else:
                result.next = ListNode(i)
                result = result.next

        print(finalList)
        return finalList





soln = Solution()
soln.mergeTwoLists(linkedList, linkedList2)


# BEST SOLUTION
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(-1)
#         res_tail = dummy
#         while list1 and list2:
#             if list1.val < list2.val:
#                 res_tail.next = list1
#                 list1 = list1.next
#             else:
#                 res_tail.next = list2
#                 list2 = list2.next
#             res_tail = res_tail.next
#         if list1:
#             res_tail.next = list1
#         elif list2:
#             res_tail.next = list2
#         else:
#             res_tail.next = None
#         return dummy.next