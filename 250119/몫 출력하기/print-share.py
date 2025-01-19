count = 0
while True:
    n = float(input())
    if n % 2 == 0:
        count += 1
        print(int(n//2))
        if count == 3:
            break