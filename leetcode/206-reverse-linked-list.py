# recursion approach

class Solution:
    def recurse(self, head, parent):
        if head.next:
            new_node, old_node = self.recurse(head.next, head)
            if old_node is None:
                old_node = new_node
            new_node.next = ListNode(head.val)
            return new_node.next, old_node
        else:
            return ListNode(head.val), None
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif head and not head.next:
            return head
        elif head and head.next and not head.next.next:
            head.next.val, head.val = head.val, head.next.val
            return head
        else:
            node, new_head = self.recurse(head.next, head)
            node.next = ListNode(head.val)
            return new_head
