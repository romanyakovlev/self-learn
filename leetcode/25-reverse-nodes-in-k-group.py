# first approach

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        cur_group_tail, cur_group_head = None, None
        prev_group_tail, first_group_head = None, None
        prev = None
        while head:
            # in-place reversal
            if c == 0:
                prev_group_tail = cur_group_tail
                cur_group_tail = head
            cur, head = head, head.next
            cur.next = prev
            c += 1
            # when group is finished - connect previous group tail 
            # with current group head and set previous node to None
            if c == k:
                if not first_group_head:
                    first_group_head = cur
                cur_group_head = cur
                if prev_group_tail:
                    prev_group_tail.next = cur_group_head
                prev = None
                c = 0
            else:
                prev = cur
        # if end of linked list is not group - re-reverse last part 
        # and connect with previous group tail
        if c != 0:
            head, prev = prev, None
            while head:
                cur = head
                head = head.next
                cur.next = prev
                prev = cur
            prev_group_tail.next = prev
        return first_group_head
