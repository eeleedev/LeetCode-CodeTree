n = int(input())
c = 0
def f(n):
    global c
    if n == 1:
        return c
    if n % 2 == 0:
        c += 1
        return f(n // 2)
    else:
        c += 1
        return f(n * 3 + 1)

print(f(n))