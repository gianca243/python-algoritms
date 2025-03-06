"""My approach"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        pos = 0
        fast = head
        slow = head
        while fast.next is not None or slow.next is not None:
            pos += 1
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            else:
                fast = fast.next
            if fast is None:
                return False
            if slow == fast:
                return True

        return False

# learned approach

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
