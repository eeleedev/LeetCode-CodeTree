N = int(input())

def add_all_up(n):
    if n == 1:
        return 1
    return add_all_up(n-1)+n

print(add_all_up(N))