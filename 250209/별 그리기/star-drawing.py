n = int(input())

for i in range(n-1, -1, -1):
    for j in range(i):
        print(" ", end='')

    for j in range((2*n-1)-(2*i)):
        print('*', end='')
    print()

for i in range(1,n):
    for j in range(i):
        print(" ", end='')

    for j in range((2*n-1)-(2*i)):
        print('*', end='')
    print()

