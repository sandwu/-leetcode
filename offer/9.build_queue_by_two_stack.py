





class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, element):
        self.stack1.append(element)

    def delete_head(self):
        if len(self.stack2) != 0:
            return self.stack2.pop()
        else:
            while self.stack1:
                element = self.stack1.pop()
                self.stack2.append(element)
            if self.stack2:
                return self.stack2.pop()

s = Solution()
s.append_tail(1)
s.append_tail(2)
s.append_tail(3)
s.append_tail(4)
s.append_tail(5)
s.append_tail(6)

print(s.delete_head())
print(s.delete_head())
print(s.delete_head())
print(s.delete_head())
