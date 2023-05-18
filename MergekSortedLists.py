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
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result = newList = None
        for i in lists:
            if result is not None and result.next is None:
                result.next = i
            while i:
                if result is None:
                    result = newList = i
                else:
                    i = i.next
                    if result.next is not None:
                        result = result.next
        firstNode = newList
        while firstNode:
            finalNode = firstNode.next
            while finalNode is not None:
                if firstNode.data > finalNode.data:
                    temp = firstNode.data
                    firstNode.data = finalNode.data
                    finalNode.data = temp
                finalNode = finalNode.next
            firstNode = firstNode.next

        return newList


solution = Solution()
solution.mergeKLists([linkedList2.head, linkedList.head])

#
# BEST Solution

#
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#
#         if not lists or len(lists) == 0: return None
#
#         while len(lists) != 1:
#             merged_lists = []
#             for r in range(0, len(lists), 2):
#                 l1 = lists[r]
#                 l2 = lists[r + 1] if r + 1 < len(lists) else None
#                 l3 = self.merge_two_lists(l1, l2)
#                 merged_lists.append(l3)
#             lists = merged_lists
#
#         return lists[0]
#
#     def merge_two_lists(self, l1, l2):
#         dummy = prev = ListNode()
#
#         while l1 and l2:
#             if l1.val < l2.val:
#                 prev.next = l1
#                 prev = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 prev = l2
#                 l2 = l2.next
#         if l1 or l2:
#             prev.next = l1 if l1 else l2
#
#         return dummy.next
#
