n = int(input())
arr = list(map(int, input().split()))
medium_arr = []
# Write your code here!
if len(arr) == 1:
    print(arr[0])
else:
    for i in range(0, len(arr),2):
        new_arr = arr[:i+1]
        new_arr.sort()
        medium_arr.append(new_arr[len(new_arr)//2])
            

result = ' '.join(map(str,medium_arr))
print(result)