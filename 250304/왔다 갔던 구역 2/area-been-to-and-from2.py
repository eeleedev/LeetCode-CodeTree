n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
lines = [0] * 202 # -100 ~ 100
OFFSET = 100 # 0 좌표를 100으로 매핑

current = 0

for i in range(n):
    move = x[i] if dir[i] == 'R' else -x[i]
    prev = current
    new = current + move

    start = min(prev, new)
    end = max(prev, new)

    # start부터 end-1까지 각 정수 j에 대해 구간 j→j+1 방문
    for j in range(start, end):
        lines[j + OFFSET] += 1

    current = new

# 2번 이상 방문된 선분(구간)의 개수
answer = sum(1 for cnt in lines if cnt >= 2)
print(answer)
