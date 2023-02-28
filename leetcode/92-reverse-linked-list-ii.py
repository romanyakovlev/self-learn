# first approach

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter = 0
        start = head
        # iter until reach left
        while left > (counter + 1):
            left_tail = head
            head = head.next
            counter += 1
        reverse_tail = head
        prev = None
        # reverse LL until reach right
        while right > counter:
            reverse_head = head
            head = head.next
            reverse_head.next = prev
            prev = reverse_head
            counter += 1
        # connect reversed LL tail with LL head after right
        reverse_tail.next = head
        # check that LL is not reversed from start (left != 0)
        if start is not reverse_tail:
            # if yes - connect reversed LL tail with LL tail before left
            left_tail.next = reverse_head
            return start
        else:
            return reverse_head
    
        
