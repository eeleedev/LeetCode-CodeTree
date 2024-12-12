arr = list(map(float, input().split()))
Sum = 0
for elem in arr:
    Sum += elem

print(round(Sum/8,1))
