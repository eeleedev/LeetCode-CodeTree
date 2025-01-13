import sys

min_value = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))
count = 0


for elem in arr:
    if elem < min_value:
        min_value = elem

for elem in arr:
    if elem == min_value:
        count +=1

print(min_value, count)
    
