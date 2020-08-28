from binarytree import Node
root = Node(5)
root.left = Node(2)
root.right = Node(-3)


class Solution:
    def __init__(self):
        self.result = {}

    def findFrequentTreeSum(self, root):
        queue = [root]
        while queue:
            top = queue.pop(0)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
            current_sum = self.Treesum(top)
            if str(current_sum) not in self.result.keys():
                self.result[current_sum] = 1
            else:
                self.result[current_sum] += 1
        result = sorted(self.result.items(), key=lambda item: item[1])
        result.reverse()
        print(result)
        total = []
        maxnum = result[0][1]
        for ele in result:
            if ele[1] == maxnum:
                total.append(int(ele[0]))
        return total

    def Treesum(self, root):  # 求一颗树所有节点元素的和
        if not root:
            return 0
        return root.value + self.Treesum(root.left) + self.Treesum(root.right)

s = Solution()
print(s.findFrequentTreeSum(root))
# print(s.Treesum(root))



