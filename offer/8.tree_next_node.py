


"""

给定二叉树和其一个节点，求出他的下一个节点

1.二叉树为空，则返回空；

2.节点右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着指向左子结点的指针找到的叶子节点即为下一个节点；

3.节点不是根节点。如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。
"""

class Solution:
    def getNext(self, pNode):
        if pNode.right:  # 如果一个节点存在右子树，下一个节点为它的右子树中的最左子节点
            tmpNode = pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left
            return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next:  # tmpnode.next即表示是其父节点，所以root要增加一个self.next=None，标识其父节点
                if tmpNode.next.left == tmpNode:  # 这里意味着父节点的左节点是否是本节点，是的话直接返回父节点
                    return tmpNode.next
                tmpNode = tmpNode.next
            return None
