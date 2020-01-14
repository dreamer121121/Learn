from binarytree import Node
class Solution():
    def generateTrees(self,n):
        if n == 0:
            return []
        def build_Trees(left,right):
            all_trees = []
            if (left>right):#递归边界条件
                return [None] #以列表的方式返回。
            for i in range(left,right+1):
                left_trees = build_Trees(left,i-1)
                right_trees = build_Trees(i+1,right)
                #重组左右BST并将当前的节点添加进去
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = Node(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            return all_trees
        res = build_Trees(1,n)
        return res
s = Solution()
print(s.generateTrees(3))
for root in s.generateTrees(3):
    print(root)
