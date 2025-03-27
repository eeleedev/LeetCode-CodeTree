n = int(input())
arr = [input() for _ in range(n)]

tot1 = 0
tot2 = 0
for elem in arr:
    tot1 += len(elem)
    if elem[0] == 'a':
        tot2 += 1

print(tot1, tot2)
