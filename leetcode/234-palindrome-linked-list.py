# first solution

class Solution:
    def changeLinkedListDirection(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_next = head.next
        head.next = None
        while prev_next:
            prev, head = head, prev_next
            prev_next, head.next = head.next, prev
        return head
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        if fast and not fast.next:
            return True
        while fast and fast.next and fast.next.next:
            prev_slow = slow
            slow, fast = slow.next, fast.next.next
        head2 = prev_slow.next if not fast.next else slow.next
        head1, head2 = head, self.changeLinkedListDirection(head2)
        while head1 and head2:
            val1, val2 = head1.val, head2.val
            if val1 != val2:
                return False
            head1, head2 = head1.next, head2.next
        return True
