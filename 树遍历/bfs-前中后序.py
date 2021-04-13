

def pre_order(root):
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        res.append(node.value)
        stack.append(node.right)
        stack.append(node.left)
    return res


def in_order(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.value)
        root = node.right


def post_order(root):
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        res.append(node.value)
        stack.append(node.left)
        stack.append(node.right)
    return res[::-1]



class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Tree(10)
b = Tree(11)
c = Tree(12)
d = Tree(13)
e = Tree(14)

a.left = b
a.right = c
b.left = d
b.right = e

print(pre_order(a))
print(in_order(a))
print(post_order(a))
