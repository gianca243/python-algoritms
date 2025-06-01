"""
My first solution:
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ans = ListNode(head.val, None)
        node = ans

        while head:
            if head.val != ans.val:
                ans.next = ListNode(head.val, None)
                ans = ans.next
            head = head.next

        return node


class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head

        while curr:
            if curr.next:
                _next = curr.next
                while _next and curr.val == _next.val:
                    _next = _next.next
                curr.next = _next

            curr = curr.next

        return head
