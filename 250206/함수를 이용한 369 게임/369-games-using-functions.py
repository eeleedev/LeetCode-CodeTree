a, b = map(int, input().split())

def tsn(num):
    temp1 = num // 10
    temp2 = num % 10
    if temp1 == 3 or temp1 == 6 or temp1 == 9:
        return True
    elif temp2 == 3 or temp2 == 6 or temp2 == 9:
        return True
    else:
        return False

def count_func(a,b):
    counter = 0
    for i in range(a,b+1):
        if tsn(i):
                counter += 1
        elif i%3==0:
            counter += 1
    return counter

print(count_func(a,b))
