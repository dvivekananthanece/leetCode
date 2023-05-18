from LeetCode import linkedList as ll
from typing import Optional

linkedList = ll.head()
linkedList.head = ll.Node(7)
Node2 = ll.Node(2)
Node3 = ll.Node(4)
Node4 = ll.Node(3)
linkedList.head.next = Node2
Node2.next = Node3
Node3.next = Node4

linkedList2 = ll.head()
linkedList2.head = ll.Node(5)
Node9 = ll.Node(6)
Node8 = ll.Node(4)
linkedList2.head.next = Node9
Node9.next = Node8


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        newList = None
        while l1:
            list1.append(l1.data)
            l1 = l1.next
        while l2:
            list2.append(l2.data)
            l2 = l2.next
        carry = 0
        result = None
        while list1 or list2 or carry:
            obj1 = list1.pop() if list1 else 0
            obj2 = list2.pop() if list2 else 0
            carry, val = divmod(obj1+obj2+carry,10)

            newList =  ListNode(val)
            newList.next = result
            result = newList
        return newList



solution = Solution()
solution.addTwoNumbers(linkedList.head,linkedList2.head)