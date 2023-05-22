class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddNode = ListNode()
        retunNode = oddNode
        evenNode = ListNode()
        joinNode = evenNode
        i = 1
        while head:
            if i % 2 != 0:
                oddNode.next = ListNode(head.val)
                oddNode = oddNode.next
                i += 1
            else:
                evenNode.next = ListNode(head.val)
                evenNode = evenNode.next
                i += 1
            head = head.next
        oddNode.next = joinNode.next
        return retunNode.next
