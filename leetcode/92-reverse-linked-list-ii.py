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
    
        
# solution from disc

"""
Here is a step-by-step breakdown of how the code works:

The function takes in three parameters: head, which is the head of the linked list; left, 
which is the starting index of the sublist to be reversed; and right, which is 
the ending index of the sublist to be reversed.

A new ListNode object called dummy is created with a value of 0. 
This node will serve as a dummy head node for the linked list.

The next attribute of the dummy node is set to head. 
This makes the dummy node the new head of the linked list.

Two pointer variables, pre and cur, are initialized to dummy. 
These pointers will be used to locate the nodes at the left and right indices.

A loop is executed left-1 times to move the pre and cur pointers to the correct positions. 
At the end of the loop, pre will be pointing to the node immediately before the left index, 
and cur will be pointing to the node at the left index.

Another loop is executed right-left times to reverse the sublist between left and right. 
Inside the loop, a temporary variable called temp is created to hold the next node in the list. 
Then, the next attribute of cur is set to temp.next, effectively removing temp from the sublist. 
The next attribute of temp is then set to pre.next, effectively inserting temp into the sublist immediately after pre. 
Finally, the next attribute of pre is set to temp, effectively connecting pre to the newly inserted node.

After the loop has completed, the function returns the next attribute of the dummy node, 
which is the head of the modified linked list.

Overall, the function reverses a sublist of a linked list between the left and right 
indices by manipulating pointers and node connections.
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        # find the position
        for i in range(1,left):
            cur = cur.next
            pre = pre.next
        print(cur.val, pre.val)
        # reverse
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next
