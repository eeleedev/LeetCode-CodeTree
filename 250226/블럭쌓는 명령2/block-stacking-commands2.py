n, k = map(int, input().split()) # n: 전체 칸 개수 k: 명령 개수
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
block = [0] * n # 빈 블럭 생성

for i in range(k): # 명령 수만큼 반복
    for j in range(commands[i][0],commands[i][1]+1):
        block[j-1] += 1

print(max(block))
