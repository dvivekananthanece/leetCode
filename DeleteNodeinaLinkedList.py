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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next






soln = Solution()
soln.deleteNode(linkedList.head)