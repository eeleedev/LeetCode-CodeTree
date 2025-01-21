count = 0
n = int(input())
while True:
    if n == 1:
        print(count)
        break
    elif n % 2 == 0:
        n //= 2
        count += 1
        if n == 1:
            print(count)
            break
    else:
        n = n*3 + 1
        count += 1
        if n == 1:
            print(count)
            break

