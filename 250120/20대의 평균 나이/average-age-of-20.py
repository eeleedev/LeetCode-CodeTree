arr = []
while True:
    n = float(input())
    if n < 30:
        arr.append(n)
    else:
        temp = 0
        for figure in arr:
            temp += figure
        print(f"{temp/len(arr):.2f}")
        break