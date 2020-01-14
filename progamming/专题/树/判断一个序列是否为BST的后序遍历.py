class Solution():
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        root = sequence[-1] #取出当前根节点。
        #根据根节点划分数组
        index = 0 #记录右子树的起点
        for i in range(len(sequence)):
            if sequence[i] < root:
                index = i
            else:
                break
        l_array= sequence[:index]
        r_array = sequence[index:len(sequence)-1]
        for ele in r_array:
            if ele < root:
                return False #递归终止条件
        l = True
        r = True
        if len(l_array) > 0:
            l = self.VerifySquenceOfBST(l_array)
        if len(r_array) > 0:
            r = self.VerifySquenceOfBST(r_array)
        return l and r


s = Solution()
s.VerifySquenceOfBST([1,4,3,6,9,8,5])