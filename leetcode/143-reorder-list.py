# first solution

class Solution:
    def reverseList(self, head):
        start = prev = head
        head = head.next
        while head:
            prev_next, head.next = head.next, prev
            prev, head = head, prev_next
        start.next = None
        return prev

    def insertNodes(self, head, fast):
        while fast:
            prev_head, head.next, fast = head.next, fast, fast.next
            head.next.next, head = prev_head, prev_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast is head:
            return None
        head_reversed = self.reverseList(slow.next)
        slow.next = None
        self.insertNodes(head, head_reversed)
        return None


# solution from disc

class Solution:

    # Merges in place two lists
    # @return The newly merged list.
    def _mergeLists(self, a, b):
        tail = head = a
        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
        return head

    # Splits in place a list in two halves, the first half is >= in size than the second.
    # @return A tuple containing the heads of the two halves
    def _splitList(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    # Reverses in place a list.
    # @return Returns the head of the new reversed list
    def _reverseList(self, head):
        last = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode
        return last

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        a, b = self._splitList(head)
        b = self._reverseList(b)
        head = self._mergeLists(a, b)

# 2nd solution

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        middle, slow.next, prev = slow.next, None, None
        while middle:
            cur = middle
            middle = middle.next
            cur.next = prev
            prev = cur
        head_reversed = prev
        while head_reversed:
            cur1, cur2 = head.next, head_reversed.next
            head.next, head_reversed.next = head_reversed, cur1
            head, head_reversed = cur1, cur2

# from disc

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
