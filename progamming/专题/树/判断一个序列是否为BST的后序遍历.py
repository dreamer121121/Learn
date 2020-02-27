#分析：根剧BST的性质，若该数组为BST的后序遍历则最后一个值就是BST的根节点。
#从前向后遍历数组直到元素的值大于根节点，则该索引之前都为根节点的左子树，
# 从该索引开始都是根节点的右子树。检查右子树的值是否都大于根节点若假，则可判断该数组不是
#BST的后序遍历。同理对根节点的左右子树都应进行同样的判断----》递归实现。



class Solution():
    def VerifySquenceOfBST(self, sequence):
        if not sequence:#主要为了防止一开始输进来的数组为空[]，并不是递归终止条件
            return False

        return self.Verify(sequence)

    def Verify(self,sequence):
        if len(sequence) <= 1:#只有一个元素则为BST，BST
            return True
        root = sequence[-1] #取出当前根节点。
        #根据根节点划分数组
        index = 0 #记录右子树的起点
        for i in range(len(sequence)):
            if sequence[i] < root:
                index = i
            else:
                break
        l_array= sequence[:index+1]
        r_array = sequence[index+1:len(sequence)-1]
        for ele in r_array:
            if ele < root:
                return False #递归终止条件
        l = self.Verify(l_array)
        r = self.Verify(r_array)
        return l and r

s = Solution()
s.VerifySquenceOfBST([1,4,3,6,9,8,5])