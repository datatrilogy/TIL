# 선생님 풀이


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for row in range(10)] for col in range(10)]

    counter = 0
    for row in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
             for c in range(c1, c2+1):
                matrix[r][c] += color

    print(f'#{tc} {counter}')
