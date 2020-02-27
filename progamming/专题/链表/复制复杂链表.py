
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        pNode = pHead
        if pHead is None:
            return None
        """按原顺序复制节点。"""
        while pNode:
            pcloned = RandomListNode(0)
            pcloned.label = pNode.label
            pcloned.next = pNode.next
            pcloned.random = None
            pNode.next = pcloned
            pNode = pcloned.next
        """按原顺序复制节点"""

        """将原链表的random复制给新的链表"""
        pNode = pHead
        while pNode:
            pcloned = pNode.next
            if pNode.random:
                pcloned.random = pNode.random.next
            pNode = pcloned.next

        """将链表进行拆分"""
        pNode = pHead
        pclonedHead = pNode.next
        pclonedFirst = pclonedHead #用来保存复制链表的第一个节点。
        while pclonedHead.next:
            pNode.next = pclonedHead.next
            pNode = pclonedHead.next
            pclonedHead.next = pNode.next
            pclonedHead = pclonedHead.next
        pNode.next = None
        return pclonedFirst






















