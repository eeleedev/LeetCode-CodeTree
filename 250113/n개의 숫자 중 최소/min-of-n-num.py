import sys

min_value = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))
count = 1


for elem in arr:
    if elem < min_value:
        min_value = elem
    elif elem == min_value:
        count += 1

print(min_value, count)
    
