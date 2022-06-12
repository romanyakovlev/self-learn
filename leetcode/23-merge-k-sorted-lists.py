# My solution - uses dict with LinkedList value as keys and set of indexes of LinkedList in lists variable as values
# so we can
# 1. iterate through all items in lists
# 2. add data to dict 
# 3. end iteration
# 4. find min LinkedList value as dict key
# 5. merge the sequence of LinkedList with the same values to root node
# 6. check if node has next node - if yes - write to dict 
# 7. repeat until the end of all nodes from lists value

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root_node = ListNode()
        start_node = root_node
        lists_dict = {}
        lists_counter = 0
        non_empty_lists_len = len([l for l in lists if l is not None])
        for i in range(len(lists)):
            if lists[i]:
                if lists[i].val not in lists_dict:
                    lists_dict[lists[i].val] = set()
                lists_dict[lists[i].val].add(i)
        if len(lists_dict) == 0:
            return start_node.next
        while lists_counter != non_empty_lists_len:
            min_i = list(lists_dict)[0]
            for i in lists_dict.keys():
                if min_i > i:
                    min_i = i
            for node_index in lists_dict[min_i].copy():
                root_node.next = ListNode(val=lists[node_index].val)
                root_node = root_node.next
                lists[node_index] = lists[node_index].next
                lists_dict[min_i].remove(node_index)
                if lists[node_index]:
                    if lists[node_index].val not in lists_dict:
                        lists_dict[lists[node_index].val] = set()
                    lists_dict[lists[node_index].val].add(node_index)
                else:
                    lists_counter += 1
            if len(lists_dict[min_i]) == 0:
                lists_dict.pop(min_i)
        return start_node.next
