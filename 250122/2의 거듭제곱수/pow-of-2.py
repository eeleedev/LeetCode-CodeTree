n = int(input())
count = 0
while True:
    n //= 2
    count += 1
    if n == 1:
        print(count)
        break