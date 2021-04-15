

class Node:
    def __init__(self, val):
        self.val = val
        self.next  = None


a = Node(10)
b = Node(11)
c = Node(12)
d = Node(13)
e = Node(14)
f = Node(15)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = None


def traversal(head):
    """traversal linked list， so can get work"""
    res = [head.val]
    while head.next:
        res.append(head.next.val)
        head = head.next
    return res


print(traversal(a))


def reverse(head):
    """reverse linked list"""
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


print(traversal(reverse(a)))


def middlenode(head):
    """detect ring is existed or not"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


print(middlenode(a).val)


def deletenode(node):
    """delete the node"""
    node.val = node.next.val
    node.next = node.next.next


deletenode(e)
print(traversal(a))


def findNthfromend(head, n):
    """delete Nth node from end"""
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head


print(traversal(findNthfromend(a, 5)))
