"""my solution"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        prev = None
        cent = 1
        if left == right:
            return head
        def reverse(_head: Optional[ListNode]):
            nonlocal cent
            _prev = None
            _current = _head
            _end = None
            while cent <= right:
                if cent == left:
                    _end = _current
                next = _current.next
                _current.next = _prev
                _prev = _current
                _current = next
                cent += 1
            return next, _prev, _end
        while current:
            if cent < left or cent > right:
                prev = current
                current = current.next
            else:
                next, _list, end = reverse(current)
                if left > 1:
                    prev.next = _list
                else:
                    head = _list

                end.next = next
                current = end.next
            cent += 1
        return head

# linked_list = ListNode(1, ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
linked_list = ListNode(3, ListNode(5,ListNode(7)))
print( linked_list )

Solution().reverseBetween(linked_list,2,3)
