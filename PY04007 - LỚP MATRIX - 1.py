# I'm DengHwee or you can call me Chimmey
import math

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def transpose(self):
        return [[self.matrix[j][i] for j in range(self.n)] for i in range(self.m)]

    def calc(self):
        transpose_matrix = self.transpose()
        res_matrix = [[0] * n for _ in range(n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    res_matrix[i][j] += self.matrix[i][k] * transpose_matrix[k][j]
        for i in range(n):
            for j in range(n):
                print(res_matrix[i][j], end = ' ')
            print()


for i in range(int(input())):
    n, m = list(map(int, input().split()))
    a = Matrix(n, m)
    for i in range(n):
        row_values = list(map(int, input().split()))
        a.matrix[i] = row_values
    a.calc()
