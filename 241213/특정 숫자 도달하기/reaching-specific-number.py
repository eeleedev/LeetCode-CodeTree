arr = list(map(int, input().split()))
n = len(arr)

def find_the_end(n):
    for i in range(n):
        if arr[i] >= 250 :
            return i

end = find_the_end(n)

arr_new = arr[0:end]
all_sum = 0
for i in arr_new:
    all_sum += i
print(all_sum, round(all_sum/len(arr_new),1))