# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter1 = counter2 = 1
        node1 = node2 = origin_head = head
        while node1.next:
            node1 = node1.next
            counter1 += 1
        if counter1 == n:
            return origin_head.next 
        else:
            while counter1 >= counter2 + n:
                old_node = node2
                node2 = node2.next
                counter2 += 1
            old_node.next = node2.next
            return origin_head
            

 # solution from disc

 class Solution:
     def removeNthFromEnd(self, head, n):
         fast = slow = head
         for _ in range(n):
             fast = fast.next
         if not fast:
             return head.next
         while fast.next:
             fast = fast.next
             slow = slow.next
         slow.next = slow.next.next
         return head
