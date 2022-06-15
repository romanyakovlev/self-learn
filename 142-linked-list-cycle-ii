# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# first solution - O(1) memory

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start_node = head
        node1 = head
        target_node = None
        while head is not None and head.next is not None:
            node1 = node1.next
            head = head.next.next
            if node1 is head:
                target_node = node1
                break
        if target_node is None:
            return None
        while start_node is not target_node:
            temp_node = target_node.next
            while temp_node is not target_node:
                if temp_node is start_node:
                    return start_node
                temp_node = temp_node.next
            start_node = start_node.next
        return target_node
