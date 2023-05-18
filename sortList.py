from LeetCode import linkedList as ll
from typing import Optional

linkedList = ll.head()
linkedList.head = ll.Node(10)
Node2 = ll.Node(70)
Node3 = ll.Node(20)
Node4 = ll.Node(40)
Node6 = ll.Node(10)
linkedList.head.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node6
class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        finalNode = head.next
        firstNode = head
        while firstNode:
            finalNode = firstNode.next
            while finalNode is not None:
                if firstNode.data > finalNode.data:
                    temp = firstNode.data
                    firstNode.data = finalNode.data
                    finalNode.data = temp
                finalNode = finalNode.next
            firstNode = firstNode.next
        return finalNode

solution = Solution()
solution.sortList(linkedList.head)

# Best practice
#
#
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
#         lis = []
#         while curr:
#             lis.append(curr.val)
#             curr = curr.next
#
#         lis.sort()
#         current = head
#         for i in lis:
#             current.val = i
#             current = current.next
#
#         return head
#
#
