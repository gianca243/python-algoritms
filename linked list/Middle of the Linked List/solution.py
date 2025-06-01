"""
https://leetcode.com/problems/middle-of-the-linked-list/
first try:
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        s = head
        if s.next is None:
            return s
        f = head.next
        while f:
            s = s.next
            f = f.next
            if f is not None:
                f = f.next
        return s
