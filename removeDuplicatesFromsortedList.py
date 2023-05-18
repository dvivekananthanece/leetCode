from LeetCode import linkedList as ll
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


linkedList = ll.head()
linkedList.head = ll.Node(1)
Node2 = ll.Node(1)
Node3 = ll.Node(10)
Node4 = ll.Node(10)
Node6 = ll.Node(1)
linkedList.head.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node6


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        result = newList = None
        while head:
            if head.data not in list:
                list.append(head.data)
            head = head.next
        for i in list:
            if result is None:
                newList = result = ListNode(i)
            else:
                result.next = ListNode(i)
                result = result.next
        return newList

soln = Solution()
soln.deleteDuplicates(linkedList.head)

# BEST SOLUTION
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = head
#         while(node):
#             while node.next and node.val == node.next.val:
#                 node.next = node.next.next
#             node = node.next
#         return head