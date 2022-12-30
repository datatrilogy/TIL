import sys
sys.stdin = open('input.txt')

def solution(N):
    matrix  = [[0 for _ in range(N)] for _ in range(N)]
    number = 1
    row = col = 0
    move = +1

    for i in range(N, 0, -1):
        if i == 1:
            matrix[row][col] = number
        else:
            for k in range(i):
                matrix[row][col] = number
                number += 1
                if k == i - 1:
                    row += move

                else:
                    col += move

            for k in range(i-1):
                matrix[row][col] = number
                number += 1

                if k == i - 2:
                    move *= -1
                    col += move

                else:
                    row += move
    return '\n'.join([' '.join(map(str, row)) for row in matrix])

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}\n{solution(int(input()))}')