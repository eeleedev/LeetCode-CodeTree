n = int(input())
arr = list(map(float, input().split()))

Sum = 0
for elem in arr:
    Sum += elem

avg = round(Sum/n,1)

if avg >= 4.0:
    print(avg)
    print("Perfect")
elif avg >= 3.0:
    print(avg)
    print("Good")
else:
    print(avg)
    print("Poor")