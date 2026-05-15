class Solution:
    def isDup(self, l):
        return len(l) != len(set(l))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]
        squares = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i].append(num)
                    cols[j].append(num)
                    squares[(i//3)*3 + (j//3)].append(num)

        for i in range(n):
            if self.isDup(rows[i]) or self.isDup(cols[i]) or self.isDup(squares[i]):
                return False

        return True