# from LeetCode import linkedList as ll
# from typing import Optional
#
# # ll.linkedList
# linkedList = ll.head()
# linkedList.head = ll.Node(1)
# Node2 = ll.Node(2)
# Node3 = ll.Node(3)
# Node4 = ll.Node(4)
# Node6 = ll.Node(10)
# linkedList.head.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node6
#
#
#
# class ListNode:
#     pass
#
#
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         lastNode = head
#         count = 0
#         while lastNode.next is not None:
#             lastNode = lastNode.next
#             count += 1
#         lastNode = head
#         count = count - n
#         while count != 0:
#             lastNode = lastNode.next
#             count -= 1
#         if lastNode == head:
#             return head
#         if lastNode.next.next is not None:
#             lastNode.next = lastNode.next.next
#             return head
#         lastNode.next = None
#         return head
#         printData = head
#         while printData is not None:
#             print(printData.data)
#             printData = printData.next
#
#
# solution = Solution()
# solution.removeNthFromEnd(linkedList.head, 2)
#

from LeetCode import linkedList as ll
from typing import Optional

# ll.linkedList
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


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head


solution = Solution()
solution.removeNthFromEnd(linkedList.head, 2)

