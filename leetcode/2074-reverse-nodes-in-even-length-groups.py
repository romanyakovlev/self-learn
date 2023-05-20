# 1st solution

class Solution:
    def reverseCurrentGroup(self, prev_group_tail: ListNode, count: int):
        head = cur_group_tail = prev_group_tail.next
        cur_group_count = 0
        prev = None
        while head and count != cur_group_count:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
            cur_group_count += 1
        prev_group_tail.next, cur_group_tail.next = cur, head
        return cur_group_tail

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_group_count = 0
        group_count = 1
        dummy = prev_group_tail = ListNode(next=head)
        while head:
            cur_group_count += 1
            if group_count == cur_group_count:
                if group_count % 2 == 0:
                    head = self.reverseCurrentGroup(prev_group_tail, group_count)
                prev_group_tail = head
                cur_group_count = 0
                group_count += 1
            head = head.next
        if cur_group_count != 0 and cur_group_count % 2 == 0:
            self.reverseCurrentGroup(prev_group_tail, cur_group_count)
        return dummy.next
