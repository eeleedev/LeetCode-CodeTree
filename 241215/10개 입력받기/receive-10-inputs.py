arr = list(map(int, input().split()))
total = 0

def find_index(arr):
    for elem in arr:
        if elem == 0:
            return arr.index(0)
    else:
        return -1

index = find_index(arr)
def summing(index):
    global total
    if index == -1:
        for elem in arr:
            total += elem
    else:
        for elem in arr[0:index]:
            total += elem
    return total
        
summ = summing(index)
if index == -1:
    avg = summ/len(arr)
else:
    avg = summ/len(arr[0:index])
print(summ, round(avg,1))