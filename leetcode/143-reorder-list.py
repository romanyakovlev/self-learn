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
        fast = head
        slow = head
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
