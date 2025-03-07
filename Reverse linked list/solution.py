from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            head.next = next
        return prev

linked_list = ListNode(1, ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
print( linked_list )

Solution().reverseList(linked_list)
