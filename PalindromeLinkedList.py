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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = ""
        while head:
            list = list+str(head.data)
            head = head.next
        return list == list[::-1]



soln = Solution()
soln.isPalindrome(linkedList.head)