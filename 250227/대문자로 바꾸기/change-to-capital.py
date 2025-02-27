n = 5
k = 3
arr_2d = [
    list(input().split()) # list comprehension
    for _ in range(n)
]

for i in range(n):
    for j in range(k):
        print(arr_2d[i][j].upper(),end=' ')
    print()
