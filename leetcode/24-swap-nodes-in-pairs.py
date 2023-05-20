# 1st solution

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        while head and head.next:
            next_head = head.next
            head.next = next_head.next
            prev.next = next_head
            next_head.next = head
            prev = head
            head = head.next
        return dummy.next
