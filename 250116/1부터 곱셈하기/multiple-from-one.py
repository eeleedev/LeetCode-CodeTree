n = int(input())
result = 1
index = 0
for i in range(1, 11):
    result *= i
    index = i
    if result >= n:
        break

print(index)