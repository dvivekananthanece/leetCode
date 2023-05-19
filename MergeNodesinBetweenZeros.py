from LeetCode import linkedList as ll
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


linkedList = ll.head()
linkedList.head = ll.Node(0)
Node2 = ll.Node(3)
Node3 = ll.Node(1)
Node4 = ll.Node(0)
Node5 = ll.Node(4)
Node6 = ll.Node(5)
Node7 = ll.Node(2)
Node8 = ll.Node(0)
linkedList.head.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7
Node7.next = Node8

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        finalNode = ListNode()
        returnNode = finalNode
        startNode = head.next
        value = 0
        while startNode.next:
            value += startNode.data
            if startNode.next.data == 0:
                finalNode.next = ListNode(value)
                finalNode = finalNode.next
                value = 0
            startNode = startNode.next
        return returnNode.next

soln = Solution()
soln.mergeNodes(linkedList.head)