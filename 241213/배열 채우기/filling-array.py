arr = list(map(int,input().split()))

def find_index():
    for elem in arr:
        if elem == 0:
            return arr.index(elem)
        return -1

def final_result():
    n = find_index()
    if n != -1:
        for i in range(len(arr)-2, -1, -1):
            print(arr[i], end=" ")
    else:
        for i in range(len(arr)-2, -1, -1):
            print(arr[i], end=" ")

final_result()