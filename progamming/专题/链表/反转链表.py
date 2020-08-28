class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

def reverse(head):
    """定义函数的功能：将以head为头结点的链表反转，并返回反转后的头结点"""
    if not head or not head.next:
        return head
    newhead = reverse(head.next)
    head.next.next = head
    head.next = None
    return newhead
# print(reverse(head))
root = reverse(head)
while root:
    print(root.val)
    root = root.next

