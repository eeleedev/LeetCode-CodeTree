arr = list(map(int, input().split()))
answer = 0

for i in range(10):
    answer += arr[i]

print(answer)