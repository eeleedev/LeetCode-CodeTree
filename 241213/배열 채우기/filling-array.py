arr = list(map(int,input().split()))

def find_index():
    for elem in arr:
        if elem == 0:
            return arr.index(elem)

def final_result():
    n = find_index()
    if n != None:
        for i in range(n-1, -1, -1):
            print(arr[i], end=" ")
    else:
        for i in range(n-1, -1, -1):
            print(arr[i], end=" ")

final_result()