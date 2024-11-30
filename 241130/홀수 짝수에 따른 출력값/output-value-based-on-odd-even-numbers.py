N = int(input())

def add(n):
    if n % 2 == 0:
        if n == 2:
            return 2
        return n + add(n-2)

    else:
        if n == 1:
            return 1
        return n + add(n-2)

print(add(N))