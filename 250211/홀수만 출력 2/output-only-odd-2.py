b, a = map(int, input().split()) # 문제 잘 읽기

for i in range(b, a-1, -1):
    if i % 2 != 0:
        print(i, end=' ')