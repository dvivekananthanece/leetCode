from LeetCode import linkedList as ll
from typing import Optional


class ListNode:
    pass


linkedList = ll.head()
linkedList.head = ll.Node(1)
Node2 = ll.Node(1)
Node3 = ll.Node(10)
Node4 = ll.Node(10)
Node6 = ll.Node(1)
linkedList.head.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node6


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        firstHead = head.head
        secondHead = head.head
        currentHead = head.head

        def remove(self, node):
            prev_node = self.get_prev_node(node)
            if prev_node is None:
                self.head = self.head.next
            else:
                prev_node.next = node.next

        current1 = head.head
        while current1:
            data = current1.data
            current2 = current1.next
            while current2:
                if current2.data == data:
                    head.remove(current2)
                current2 = current2.next
            current1 = current1.next

        firstHead = head.head
        while firstHead is not None:
            secondHead = firstHead.next
            while secondHead is not None:
                if firstHead.data == secondHead.data:
                    secondHead.data = '_'
                secondHead = secondHead.next
            firstHead = firstHead.next
        firstHead = head.head
        while firstHead is not None:
            if firstHead.next is not None:
                if firstHead.next.data == '_' and firstHead.next.next is not None:
                    firstHead.next = firstHead.next.next
                elif firstHead.next.data == '_':
                    firstHead.next = None
            firstHead = firstHead.next
        firstHead = head.head
        while firstHead is not None:
            if firstHead.next is not None:
                if firstHead.next.data == '_' and firstHead.next.next is not None:
                    firstHead.next = firstHead.next.next
                elif firstHead.next.data == '_':
                    firstHead.next = None
            firstHead = firstHead.next
        text = 'ytd'


soln = Solution()
soln.deleteDuplicates(linkedList)
