import sys
sys.stdin = open('input.txt')


# 0 ~ 9 숫자가 적힌 N 장의 카드
# 가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력하라.
#


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    counts = [0] * 10
    for n in range(0, 10):
        if n in numbers:
            counts[n] += 1
    print(counts)


