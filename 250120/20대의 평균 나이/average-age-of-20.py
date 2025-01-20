arr = []
while True:
    n = float(input())
    if n >= 20 and n <=29:
        arr.append(n)

    if n < 21 or n > 29:
        temp = 0
        for figure in arr:
            temp += figure
        print(f"{temp/len(arr):.2f}")
        break