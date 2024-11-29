N = int(input())

def count_up_and_down(n):
    if n==0:
        return
    print(n, end=' ')
    count_up_and_down(n-1)
    print(n, end=' ')

count_up_and_down(N)