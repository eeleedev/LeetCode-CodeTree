n = int(input())
for i in range(0, n):
    print(('  '*abs(i-(n-1)))+('* '*((2*i)+1)), end=' ')
    print()