class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    # create a empty node
    dummy = ListNode()
    tail = dummy

    # compare the two list node when list node is empty
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        # insert the node
        tail = tail.next

    # find the not empty node
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

if __name__ == "__main__":
    # Test cases for merge two sorted lists
    def print_list(node):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        print("->".join(vals))

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))  

    merged = mergeTwoLists(l1, l2)
    print_list(merged)  