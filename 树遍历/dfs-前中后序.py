

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order(root):
    res = []
    pre_helper(root, res)
    return res


def pre_helper(root, res):
    if root:
        res.append(root.value)
        pre_helper(root.left, res)
        pre_helper(root.right, res)


def in_order(root):
    res = []
    in_helper(root, res)
    return res


def in_helper(root, res):
    if root:
        in_helper(root.left, res)
        res.append(root.value)
        in_helper(root.right, res)


def post_order(root):
    res = []
    post_helper(root, res)
    return res


def post_helper(root, res):
    if root:
        post_helper(root.left, res)
        post_helper(root.right, res)
        res.append(root.value)


a = Tree(10)
b = Tree(11)
c = Tree(12)
d = Tree(13)
e = Tree(14)

a.left = b
a.right = c
b.right = d
c.left = e

print(pre_order(a))
print(in_order(a))
print(post_order(a))
