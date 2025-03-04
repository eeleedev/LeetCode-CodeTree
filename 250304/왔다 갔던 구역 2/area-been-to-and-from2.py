n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
lines = [0] * 202 # -100 ~ 100
start_point = 100 # 0 좌표를 100으로 매핑

for i in range(n):
    if dir[i] == 'R':
        for _ in range(x[i]):
            lines[start_point] += 1
            start_point += 1  # 오른쪽으로 이동
    elif dir[i] == 'L':
        for _ in range(x[i]):
            lines[start_point] += 1
            start_point -= 1  # 왼쪽으로 이동

count = 0
for i in range(len(lines)):
    if lines[i] >= 2:
        count += 1

print(count)
