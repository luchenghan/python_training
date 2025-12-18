class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # create a empty node
    dummy = ListNode()
    tail = dummy

    # compare the two list node when list node is empty
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        # insert the node
        tail = tail.next

    # find the not empty node
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

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