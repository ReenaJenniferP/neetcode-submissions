class Solution:
    def isDup(self, l):
        return len(l) != len(set(l))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    num = board[i][j]
                    if num in rows[i] or num in cols[j] or num in squares[(i//3)*3 + (j//3)]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[(i//3)*3 + (j//3)].add(num)

        return True