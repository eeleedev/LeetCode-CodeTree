n = int(input())
a = list(map(int,input().split()))

# Write your code here!
counter = [0]*9

for elem in a:
    counter[elem-1] += 1

for elem in counter:
    print(elem)