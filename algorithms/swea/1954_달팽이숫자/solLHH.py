N = int(input())

matrix = [[0] * N for _ in range(N)]

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction_idx = 0

x, y = 0, 0

for i in range(1, N ** 2 + 1):
    new_x = x + direction[direction_idx][0]
    new_y = y + direction[direction_idx][1]

    if (0 <= new_x <= N-1) and (0 <= new_y <= N-1 ) and matrix[new_x][new_y] == 0:
        matrix[x][y] = i
        x = new_x
        y = new_y
    else:
        direction_idx = (direction_idx + 1 ) % 4
        new_x = x + direction[direction_idx][0]
        new_y = y + direction[direction_idx][1]
        matrix[x][y] = i
        x = new_x
        y = new_y

for i in range(N):
    print(matrix[i])