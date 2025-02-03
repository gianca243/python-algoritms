# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    remaining = 0
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _list = ListNode()
        
        if l1 is None:
            _list.val = 1
            return _list
        else:
            _list.val = l1.val + l2.val + self.remaining
        if _list.val > 9:
            self.remaining = 1
            _list.val -= 10
        else:
            self.remaining = 0
        
        if l1.next is not None and l2.next is not None:
            _list.next = self.addTwoNumbers(l1.next, l2.next)
        elif self.remaining == 1 or l1.next is not None or l2.next is not None:
            l1 = l1 if l2.next is None else l2
            _list.next = self.addTwoNumbers(l1.next, ListNode(0))
        return _list