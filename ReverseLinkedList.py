from LeetCode import linkedList as ll
from typing import Optional

linkedList = ll.head()
linkedList.head = ll.Node(1)
Node2 = ll.Node(2)
Node3 = ll.Node(3)
Node4 = ll.Node(4)
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headNode = head
        prev = None
        finalNode = None
        while headNode:
            finalNode = ListNode(headNode.data)
            finalNode.next = prev
            prev = finalNode
            headNode = headNode.next
        return finalNode





solution = Solution()
solution.reverseList(linkedList.head)


