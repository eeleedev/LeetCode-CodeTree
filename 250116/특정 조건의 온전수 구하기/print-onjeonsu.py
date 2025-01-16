n = int(input())

for i in range(1, n+1):
    condition1 = (i%2 == 0)
    condition2 = (i%10 == 5)
    condition3 = (i%3 == 0 and i%9 != 0)

    if not (condition1 or condition2 or condition3):
        print(i, end= ' ')