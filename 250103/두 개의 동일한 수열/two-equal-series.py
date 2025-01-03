n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code here!
sorted_a = sorted(A)
sorted_b = sorted(B)

if sorted_a == sorted_b:
    print("Yes")
else:
    print("No")