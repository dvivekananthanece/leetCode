from LeetCode import linkedList as ll
from typing import Optional

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
    def getDecimalValue(self, head: ListNode) -> int:
        list1 = []
        while head:
            list1.append(head.data)
            head = head.next
        return int("".join(map(str, list1)),2)



solution = Solution()
solution.getDecimalValue(linkedList2.head)
