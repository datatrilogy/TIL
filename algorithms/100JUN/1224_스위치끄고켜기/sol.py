import sys
sys.stdin = open('input.txt')

N = int(input())  # 스위치 개수
light = list(map(int, input().split()))  # 스위치 상태를 리스트로 받아줌
print(light)
# 0이면 1, 1이면 0으로 인덱스값 바꿔주는 함수
def switch(x, n):  # 성별 x, 학생이 부여받은 번호 n 을 함수로 받는다

        def onoff(a):
            if light[a-1] == 0:
                light[a-1] = 1
            else:
                light[a-1] = 0

        if x == 1:# 학생 성별이 남자이면
            for idx_num in range(N//n):
                # N을 n으로 나눈 몫만큼 for문 구현, 양의 정수 N범위 내에서 n의 배수 갯수만큼 for문
                onoff(n*(idx_num+1))

        else:  # 학생 성별이 여자이면
                onoff(n)
                if N < 2*n:
                    d = N - n
                else:
                    d = n - 1
                    for a in range(d+1):
                        if light[n-a-1] == light[n+a-1]:
                            onoff(n-a), onoff(n+a)

        return print(light)

for _ in range(int(input())):
    (x, n) = map(int, input().split())
    switch(x,n)
# // 몫 연산
# % 나머지

# 푸는데 여섯시간 걸림.. ㅋㅋ