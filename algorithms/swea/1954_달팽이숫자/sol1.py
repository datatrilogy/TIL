
N = 3
matrix = [[0] * N for _ in range(N)]
n = 0
row = col = -1
a = 1
for j in range(N):
    for i in range(N):
        col += 1
        matrix[row+1][col] = n+1
        n += 1
    row += 1
    matrix[row+1][col] = n+1
    n += 1

    print(n, row)

# row_d =[ 0 1 -1 0]
# col_d =[ 1 0  x s]


