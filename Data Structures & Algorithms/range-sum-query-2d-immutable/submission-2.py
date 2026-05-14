class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix) + 1
        self.cols = len(matrix[0]) + 1
        self.prefix = [[0]*self.cols for _ in range(self.rows)]
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                self.prefix[i][j] = self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)