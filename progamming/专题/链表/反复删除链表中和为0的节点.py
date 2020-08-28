class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#1, 2, -2, 3, -1, -1, -1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(-1)

def removezerosumNodes(head):
    dummy = ListNode(-1) #建立哨兵
    dummy.next = head
    pre_sum = 0
    hash = {0:dummy}
    while head:
        pre_sum += head.val
        if pre_sum in hash:
            hash[pre_sum].next = head.next
        else:
            hash[pre_sum] = head
        head = head.next
    return dummy.next

while removezerosumNodes(head):
    print(head.val)
    head = head.next
