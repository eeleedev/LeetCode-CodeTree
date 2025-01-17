arr = list(input())
mark = 0
count = 0
for i in range(0, len(arr)):
    if arr[i] == '(':
        mark = i
        for j in range(mark, len(arr)):
            if arr[j] == ')':
                count += 1

print(count)



