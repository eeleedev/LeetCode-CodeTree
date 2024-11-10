n,m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    a,b = map(int, input().split())
    temp = 0
    for i in range(a-1,b):
        temp += arr[i]
    
    print(temp)