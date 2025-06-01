"""
first try:
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        cent = False
        if list1.val <= list2.val:
            head_1 = list1
            head_2 = list2
        else:
            head_2 = list1
            head_1 = list2
            cent = True
        while head_1 and head_2:
            next1 = head_1.next
            next2 = None
            while head_1 and head_2 and next1 and head_1.val <= head_2.val <= next1.val:

                next2 = head_2.next

                head_1.next = head_2
                head_2.next = next1
                head_2 = next2
                head_1 = head_1.next

            if next1 is None:
                head_1.next = head_2
                head_2 = None

            head_1 = head_1.next

        return list1 if not cent else list2
