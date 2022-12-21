import sys
import os 
filename = os.path.join(os.path.dirname(___))
sys.stdin = open(os.getcwd() /'input.txt')   # 파일 위치 경로에서 python sol.py

T = int(input())

def solve(numbers):
    total = 0
    for num in numbers:
        if num % 2:
            total += num
    
    return total

# tc for test case
for tc in range(1, T +1):
    numbers = list(map(int, input().split()))
    answer = solve(numbers)
    print(f'#{tc} {solve(numbers)}')