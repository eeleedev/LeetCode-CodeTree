n = int(input())
all_sum = 0
index = 0
for i in range(1, 101):
    index = i
    all_sum += i
    if all_sum >= n:
        break

print(index)