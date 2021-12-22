# dumb solution 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        stop = False
        while not stop:
            if l1 and l2:
                if l1.val <= l2.val:
                    if not result:
                        result.append(ListNode(l1.val, None))
                        l1 = l1.next
                    else:
                        result.append(ListNode(l1.val, None))
                        result[-2].next = result[-1]
                        l1 = l1.next
                else:
                    if not result:
                        result.append(ListNode(l2.val, None))
                        l2 = l2.next
                    else:
                        result.append(ListNode(l2.val, None))
                        result[-2].next = result[-1]
                        l2 = l2.next
            elif l1:
                if not result:
                    result.append(ListNode(l1.val, None))
                    l1 = l1.next
                else:
                    result.append(ListNode(l1.val, None))
                    result[-2].next = result[-1]
                    l1 = l1.next
            elif l2:
                if not result:
                    result.append(ListNode(l2.val, None))
                    l2 = l2.next
                else:
                    result.append(ListNode(l2.val, None))
                    result[-2].next = result[-1]
                    l2 = l2.next
            else:
                stop = True
        return result[0] if result else l1

# recursion solution
    
class Solution:
    def recurse(self, root, list1, list2):
        if not root:
            return None
        if (list1 and list2) or (list1 and list1.next) or (list2 and list2.next):
            root.next = ListNode()
        if list1 and list2:
            if list1.val <= list2.val:
                root.val = list1.val
                self.recurse(root.next, list1.next, list2)
            else:
                root.val = list2.val
                self.recurse(root.next, list1, list2.next)
        elif list1:
            root.val = list1.val
            self.recurse(root.next, list1.next, list2)
        elif list2:
            root.val = list2.val
            self.recurse(root.next, list1, list2.next)
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        root = ListNode()
        self.recurse(root, list1, list2)
        return root
        
            

# algo with dummy node (from discussions)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
        dummy = temp = ListNode(0)
        while l1 != None and l2 != None:

            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return dummy.next

# recursion algo

class Solution:
    def getList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            if l1.val > l2.val:
                return ListNode(l2.val, self.getList(l1, l2.next)) 
            else:
                return ListNode(l1.val, self.getList(l1.next, l2))
        elif l1:
            return ListNode(l1.val, self.getList(l1.next, None))
        elif l2:
            return ListNode(l2.val, self.getList(None, l2.next))
        else:
            return None
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.getList(l1, l2)
