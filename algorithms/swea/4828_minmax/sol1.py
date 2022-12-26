
    # 내가 하고 싶은 것 numbers 리스트 안의 숫자를 하나 하나 꺼내서 비교하고, 제일 큰 수와 작은 수를 찾고 싶다.
    # 큰 수는 어떻게 찾을 수 있을까?
    # 첫 번째 항목을 꺼내서 새로 리스트에 집어넣고, 이것을 다음 숫자와 비교해서 크거나 같으면 그대로 놔두고, 다음 숫자를 할당한다.

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max = 0

    for number in numbers:
        if number > max:
            max = number
    min = max
    for number in numbers:
        if number < min:
            min = number

    ans = max - min
    print(f'#{tc} {ans}')




