n = int(input())
for i in range(n-1, -1, -1):
    print(('  '*abs(i-(n-1)))+('* '*((2*i)+1)), end=' ')
    print()