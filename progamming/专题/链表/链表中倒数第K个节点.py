from data_structure.link_list import Listnode
phead = Listnode(1)
phead.next = Listnode(2)
phead.next.next = Listnode(3)
phead.next.next.next = Listnode(4)
phead.next.next.next.next = Listnode(5)

class Solution():
    def FindKthToTail(self, head, k):
        if not head or k <= 0:
            return None
        first = head
        second = head
        for i in range(k):
            second = second.next
            if second is None: #若len(ListLink)<k ==> 返回空
                return None
        while second:
            first = first.next
            second = second.next
        return first.value
s = Solution()
print(s.FindKthToTail(phead,2))
