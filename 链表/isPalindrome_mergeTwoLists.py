

class Node:
    def __init__(self, val):
        self.val = val
        self.next  = None


a = Node(10)
b = Node(11)
c = Node(12)
d = Node(11)
e = Node(10)

a.next = b
b.next = c
c.next = d
d.next = e


def traversal(head):
    """traversal linked list， so can get work"""
    res = [head.val]
    while head.next:
        res.append(head.next.val)
        head = head.next
    return res


print(traversal(a))


def mergelink(node1, node2):
    dummy = curr = Node(0)
    while node1 and node2:
        if node1.val < node2.val:
            curr.next = node1
            node1 = node1.next
        else:
            curr.next = node2
            node2 = node2.next
        curr = curr.next
    curr.next = node1 or node2
    return dummy.next

g = Node(5)
h = Node(20)
j = Node(21)
k = Node(23)

g.next = h
h.next = j
j.next = k

print(traversal(mergelink(a, g)))


def isparlindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        curr = slow
        slow = slow.next
        curr.next = prev
        prev = curr

    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True


print(isparlindrome(a))
