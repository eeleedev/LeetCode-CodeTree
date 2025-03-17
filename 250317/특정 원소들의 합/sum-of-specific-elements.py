import sys

data = sys.stdin.read().strip().split("\n")
arr = [list(map(int,row.split())) for row in data]

result = 0
for i in range(4):
    for j in range(i+1):
        result += arr[i][j]

print(result)