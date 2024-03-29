# recursion approach (with object creation)

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
            node.next = head
            head.next = None
            return new_head

# solution using In-place Reversal of a Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, cur, next = None, head, head.next
        while next:
            cur.next = prev
            prev, cur, next = cur, next, next.next
        cur.next = prev
        return cur

# solution from disc

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
