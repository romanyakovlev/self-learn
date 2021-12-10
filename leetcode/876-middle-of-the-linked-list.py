# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        counter1 = counter2 = 1
        node1 = node2 = head
        while node1.next:
            node1 = node1.next
            counter1 += 1
        target = counter1 // 2
        while counter2 != target:
            node2 = node2.next
            counter2 += 1
        return node2.next
        
# beautiful solution by using 2 slow/fast pointers

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
