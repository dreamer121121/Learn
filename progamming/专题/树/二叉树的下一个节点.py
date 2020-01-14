class Solution():
    def GetNext(self, pNode):
        #主要把4种情况都考虑清楚。
        if not pNode:
            return
        if pNode.right:
            #有右节点存在的情况
            lf = pNode.right
            while lf:
                lf = lf.left
            return lf
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            else:
                pNode = tmp
