


class Solution:
    def func1(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

    def fun2(self, head):
        if head is None:
            return
        self.fun2(head.next)
        print(head.val)




class Root:
    def __init__(self, value):
        self.val = value
        self.next = None

a = Root(10)
b = Root(20)
c = Root(30)
d = Root(40)

a.next = b
b.next = c
c.next = d

s = Solution()
print(s.func1(a))
s.fun2(a)
