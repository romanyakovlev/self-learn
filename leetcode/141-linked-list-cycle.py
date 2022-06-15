# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution using O(1) memory

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node1 = head
        while head is not None and head.next is not None:
            node1 = node1.next
            head = head.next.next
            if node1 is head:
                return True
        return False
        
# Naive solution using set

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur_node = head
        nodes_set = set()
        while cur_node is not None:
            if cur_node in nodes_set:
                return True
            nodes_set.add(cur_node)
            cur_node  = cur_node.next
        return False
 
