"""
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，
x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，
其不需要被置于左右两部分之间。
示例:
输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(2)


class Solution():
    def partition(self, head,x):
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        nodes.sort()
        head = ListNode(nodes.pop(0))
        h = head
        while nodes:
            node = ListNode(nodes.pop(0))
            h.next = node
            h = h.next
        return head
    def partition2(self, head, x):
        left = p1 = ListNode(0)
        right = p2 = ListNode(0)
        p3 = head
        while p3:
            if p3.val < x:
                p1.next = p3
                p1 = p1.next
            elif p3.val >= x:
                p2.next = p3
                p2 = p2.next
            p3 = p3.next
        p2.next = None
        p1.next = right.next
        return left.next
s = Solution()
print(s.partition2(head,3).next.next.val)