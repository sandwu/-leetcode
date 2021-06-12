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
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if not word:return True
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != word[0]:
            return
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or \
            self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


s = Solution()
print(s.word_search(board, word1))
print(s.word_search(board, word2))
print(s.word_search(board, word3))
