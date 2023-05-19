from LeetCode import linkedList as ll
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


linkedList = ll.head()
linkedList.head = ll.Node(1)
Node2 = ll.Node(1)
Node3 = ll.Node(1)
Node4 = ll.Node(10)
Node6 = ll.Node(1)
linkedList.head.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node6

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        node = head
        prevNode = node
        currentNode = prevNode.next
        while currentNode:
            if node.data == val:
                node = currentNode
                prevNode = node
                currentNode = currentNode.next
            elif currentNode.data == val:
                prevNode.next = currentNode.next
                currentNode = prevNode.next
            else:
                prevNode = prevNode.next
                currentNode = currentNode.next
        return node


soln = Solution()
soln.removeElements(linkedList.head,1)


# Best solution
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if not head:
#             return head
#         startNode = ListNode()
#         startNode.next = head
#         ptr = startNode
#
#         while ptr.next:
#             if ptr.next.val == val:
#                 ptr.next = ptr.next.next
#                 continue
#             ptr = ptr.next
#         return startNode.next