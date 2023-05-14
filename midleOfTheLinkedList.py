import math

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
    pass


import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = head
        count = 0
        while firstNode.next is not None:
            count += 1
            firstNode = firstNode.next
        firstNode = head
        if count+1 % 2 == 0:
            test = 0
            while test != math.ceil(count / 2):
                firstNode = firstNode.next
                test += 1
            return firstNode.next
        else:
            test = 0
            while test != math.ceil(count / 2):
                firstNode = firstNode.next
                test += 1
            return firstNode


solution = Solution()
solution.middleNode(linkedList.head)

# Best Practice 11ms
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         counter = 0
#         dummyHead = head
#         while dummyHead is not None:
#             counter += 1
#             dummyHead = dummyHead.next
#         for num in range(counter // 2) :
#             head = head.next
#         return head

#mine 43ms
