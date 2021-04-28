
"""
nums = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = 'ABCCEEE' , True
word = 'ABCB', False

"""

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word1 = 'ABCCED'
word2 = 'ABCB'
word3 = 'SEE'


class Solution:
    def word_search(self, board, word):
        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        if not word: return True
        if i < 0 or j < 0 or i>len(board)-1 or j>len(board[0])-1 or board[i][j] != word[0]:
            return
        tmp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board, word[1:], i, j+1) or self.dfs(board, word[1:], i, j-1) or \
        self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i-1, j)
        board[i][j] = tmp
        return res

s = Solution()
print(s.word_search(board, word1))
print(s.word_search(board, word2))
print(s.word_search(board, word3))

