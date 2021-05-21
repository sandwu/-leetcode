

"""
前序：{1, 2, 4, 7, 3, 5, 6, 8}
中序：{4, 7, 2, 1, 5, 3, 8, 6}

根据前中序重建树


前序首字母就是根节点，中序的根节点在中间，分隔开了左子树和右子树
"""


class Root:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def tree_rebuild(self, pre_order, in_order):
        if len(pre_order) == 0 or len(in_order) == 0:
            return
        root_val = pre_order[0]
        root = Root(root_val)
        _index = in_order.index(root_val)
        root.left = self.tree_rebuild(pre_order[1:_index+1], in_order[:_index])
        root.right = self.tree_rebuild(pre_order[_index+1:], in_order[_index+1:])
        return root

a = Root(1)
b = Root(2)
c = Root(3)
d = Root(4)
e = Root(5)
f = Root(6)
g = Root(7)
h = Root(8)


pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
in_order = [4, 2, 7, 1, 5, 3, 8, 6]

s = Solution()
root1 = s.tree_rebuild(pre_order, in_order)
print(root1.val, root1.left.val, root1.left.left.val, root1.left.right.val)
