N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Write your code here!
max_count = 0

for i in range(N):
    for j in range(N-2):
        total = grid[i][j]+grid[i][j+1]+grid[i][j+2]
        if total > max_count:
            max_count = total

print(max_count)