# recursion approach

class Solution:
    def recurse(self, head):
        if head.next:
            new_node, old_node = self.recurse(head.next)
            new_node.next = head
            return new_node.next, old_node
        else:
            return head, head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            node, new_head = self.recurse(head.next)
            head.next, node.next = None, head
            return new_head
