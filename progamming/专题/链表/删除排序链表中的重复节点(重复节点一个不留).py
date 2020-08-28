class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        h = last = ListNode(-1)
        last.next = pHead
        tmp = pHead
        cur = pHead.next
        while cur:
            if tmp.val != cur.val:
                last = tmp
                tmp = cur
                cur = cur.next
            else:
                while tmp.val == cur.val:
                    cur = cur.next
                    if cur == None:
                        last.next = cur
                        return h.next
                last.next = cur
                tmp = cur
                cur = cur.next
        return h.next