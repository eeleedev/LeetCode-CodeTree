N = int(input())

def power(n):
    if n < 10:
        return n**2
    return power(n // 10)+(n % 10)**2

print(power(N))