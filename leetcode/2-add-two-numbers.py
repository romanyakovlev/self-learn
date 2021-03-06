# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution using recursion

class Solution:
    def recursion(self, end, l1, l2):
        if l1 and l2:
            s = l1.val + l2.val + end
            if s >= 10:
                return ListNode(val=s % 10, next=self.recursion(1, l1.next, l2.next))
            else:
                return ListNode(val=s, next=self.recursion(0, l1.next, l2.next))
        elif l1:
            s = l1.val + end
            if s >= 10:
                return ListNode(val=s % 10, next=self.recursion(1, l1.next, None))
            else:
                return ListNode(val=s, next=self.recursion(0, l1.next, None))
        elif l2:
            s = l2.val + end
            if s >= 10:
                return ListNode(val=s % 10, next=self.recursion(1, None, l2.next))
            else:
                return ListNode(val=s, next=self.recursion(0, None, l2.next))
        elif end == 1:
            return ListNode(val=end, next=self.recursion(0, None, None))
        else:
            return None
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursion(0, l1, l2)

# Solution using iteration

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        start_node = l
        end = 0
        while l1 or l2:
            if l1 and l2:
                s = l1.val + l2.val + end
                if s >= 10:
                    l.val = s % 10
                    end = 1
                else:
                    l.val = s
                    end = 0
                l1, l2 = l1.next, l2.next
            elif l1:
                s = l1.val + end
                if s >= 10:
                    l.val = s % 10
                    end = 1
                else:
                    l.val = s
                    end = 0
                l1 = l1.next
            elif l2:
                s = l2.val + end
                if s >= 10:
                    l.val = s % 10
                    end = 1
                else:
                    l.val = s
                    end = 0
                l2 = l2.next
            if l1 or l2:
                l.next = ListNode()
                l = l.next
            elif end == 1:
                l.next = ListNode(val=1)
                l = l.next
                end = 0
        return start_node
