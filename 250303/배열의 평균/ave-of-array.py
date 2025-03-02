n = 2
k = 4
arr_2d = []
for _ in range(n):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

for i in range(n):
    average = sum(arr_2d[i])/k
    print(round(average,2),end=' ')

print()

for i in range(k):
    average = (arr_2d[0][i]+arr_2d[1][i])/n
    print(round(average,2),end=' ')

total_sum = 0

for i in range(n):
    for j in range(k):
        total_sum += arr_2d[i][j]

print()
print(round(total_sum/8,2))