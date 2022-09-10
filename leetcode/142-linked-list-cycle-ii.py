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


# second solution - hashing approach (faster)

class Solution:
    def createCycleNodeSet(self, node: ListNode) -> set[ListNode]:
        node_set = set()
        temp_node = node.next
        node_set.add(temp_node)
        while temp_node is not node:
            temp_node = temp_node.next
            node_set.add(temp_node)
        return node_set
    
    def getFirstCycleNode(self, node: Optional[ListNode], node_set: set[ListNode]) -> ListNode:
        while node not in node_set:
            node = node.next
        return node
            
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
        else:
            return None
        cycle_node_set = self.createCycleNodeSet(target_node)
        start_cycle_node = self.getFirstCycleNode(start_node, cycle_node_set)
        return start_cycle_node

# solution from discussion    

def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head
