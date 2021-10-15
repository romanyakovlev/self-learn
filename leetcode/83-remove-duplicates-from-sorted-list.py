# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                if temp.next.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
            else:
                temp = temp.next
        return head
      
# other solutions from desc
