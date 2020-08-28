class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.Convert(pRootOfTree.left) #对左子树进行链表创建
        #将当前节点加入到链表中
        if not self.head:
            self.head,self.tail = pRootOfTree
        else:
            self.tail.right,pRootOfTree.left = pRootOfTree,self.tail
            self.tail = self.tail.right
        self.Convert(pRootOfTree.right) #对右子树进行链表创建
        return self.head
#从总体结构上看就是对中序遍历的一个改进！

