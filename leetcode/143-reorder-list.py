# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
        if not head.next:
            return None
        if head.next and not head.next.next:
            return None
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head_reversed = self.reverseList(slow.next)
        slow.next = None
        self.insertNodes(head, head_reversed)
        return None
        
