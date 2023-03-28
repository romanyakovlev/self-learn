# 1st solution

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev1 = prev2 = dummy
        cur1 = cur2 = dummy.next = head
        c1 = c2 = 1
        while c1 != k:
            c1 += 1
            prev1, cur1 = cur1, cur1.next
        c3 = c1
        head = cur1
        while head.next:
            c3 += 1
            head = head.next
        k2 = c3 - k + 1
        while c2 != k2:
            c2 += 1
            prev2, cur2 = cur2, cur2.next
        if cur1.next is not cur2 and cur2.next is not cur1:
            cur2.next, cur1.next, prev2.next, prev1.next = cur1.next, cur2.next, cur1, cur2
        elif c1 < c2:
            cur2.next, cur1.next, prev1.next = cur1.next, cur2.next, cur2
        else:
            cur2.next, cur1.next, prev2.next = cur1.next, cur2.next, cur1
        return dummy.next
