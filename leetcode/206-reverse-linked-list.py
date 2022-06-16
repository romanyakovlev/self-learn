# recursion approach (easier to understand)

class Solution(object):
    
    def recurse(self, node, next_node):
        if not node.next:
            return ListNode(val=node.val, next=next_node)
        return self.recurse(node.next, ListNode(val=node.val, next=next_node))
        
    def reverseList(self, head):
        if not head:
            return None
        elif not head.next:
            return ListNode(val=head.val, next=None)
        elif not head.next.next:
            return ListNode(val=head.next.val, next=ListNode(val=head.val, next=None))
        else:
            return self.recurse(head.next, ListNode(val=head.val, next=None))

# recursion approach (wihout object creation)

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
