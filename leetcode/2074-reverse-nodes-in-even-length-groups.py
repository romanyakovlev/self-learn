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

# 2nd solution (educative inspired)

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start from 2 because 1 is odd
        group_count = 2
        dummy = ListNode(next=head)
        while head:
            cur_group_count = 0
            prev = head
            # get group count (cur_group_count)
            for _ in range(group_count):
                if not head.next:
                    break
                cur_group_count += 1
                head = head.next
            # if group count is even - reverse it
            if cur_group_count % 2 == 0:
                cur = prev.next
                reverse = head.next
                # reverse even group (add nodes to head of the next group)
                for _ in range(cur_group_count):
                    next_cur = cur.next
                    cur.next = reverse
                    reverse = cur
                    cur = next_cur
                prev_next = prev.next
                # connect prev group tail with current group head
                prev.next = reverse
                # set head as current group tail (group tail is prev_next)
                head = prev_next
            group_count += 1
        return dummy.next
