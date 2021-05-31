

class Solution:
    def __init__(self):
        self.map = {}

    def fibonacci(self, n):
        if self.map.get(n):
            return self.map[n]
        if n <= 1:
            return n
        result = self.fibonacci(n-1) + self.fibonacci(n-2)
        self.map[n] = result
        return result

    def fibonacci2(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007


s = Solution()
print(s.fibonacci(10))
print(s.fibonacci2(10))
