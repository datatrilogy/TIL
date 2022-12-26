# SWEA 파이썬 문제해결 기본


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # max() / min() 안쓰고
    # sort => [0] / [-1]

    max_value = max(numbers)
    min_value = min(numbers)

    ans = max_value - min_value

    print(f'#{tc} 123')