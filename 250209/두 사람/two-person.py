A_a, A_s = input().split()
B_a, B_s = input().split()

A_a = int(A_a)
B_a = int(B_a)


if (A_a >= 19 and A_s == "M") or (B_a >= 19 and B_s == "M"):
    print(1)
else:
    print(0)