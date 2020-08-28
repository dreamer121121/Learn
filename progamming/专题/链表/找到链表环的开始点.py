from data_structure.link_list import Listnode
phead = Listnode(1)
phead.next = Listnode(2)
phead.next.next = Listnode(3)
phead.next.next.next = Listnode(4)
phead.next.next.next.next = Listnode(5)
phead.next.next.next.next.next = phead.next
# print(phead)
def findstart(head):
    slow = head
    fast = head
    p = None
    h = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            p = slow #相遇点
            break
    while p != h:
        h = h.next
        p = p.next
    return p
print(findstart(phead).value)
