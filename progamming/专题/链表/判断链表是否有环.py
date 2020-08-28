from data_structure.link_list import Listnode
phead = Listnode(1)
phead.next = Listnode(2)
phead.next.next = Listnode(3)
phead.next.next.next = Listnode(4)
phead.next.next.next.next = Listnode(5)
# phead.next.next.next.next.next = phead.next

def judge(head):
    if not head and head.next:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
print(judge(phead))



