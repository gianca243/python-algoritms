"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        _len = 0
        h = head
        while h:
            _len += 1
            h = h.next

        target = _len - n

        h = head
        prev = None
        cent = 0
        while h:
            if cent == target and prev:
                prev.next = h.next
            elif cent == target and prev is None:
                return head.next
            cent += 1
            prev = h
            h = h.next
        return head
