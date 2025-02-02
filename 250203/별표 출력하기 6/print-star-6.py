n = int(input())

for i in range(0, n):
    for j in range(i):   
        print(" ", end=" ")
    for j in range(2*n-(2*i)-1):
        print("*", end=" ")
    print()

for i in range(0, n-1):
    for j in range(n-i-2):   
        print(" ", end=" ")
    for j in range(n+(2*i)-1):
        print("*", end=" ")
    print()
