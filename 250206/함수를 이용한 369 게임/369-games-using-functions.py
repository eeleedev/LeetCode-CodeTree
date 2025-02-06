a, b = map(int, input().split())

def tsn(num):
    temp = list(str(num))
    for a in temp:
        if a == '3' or a=='6' or a=='9':
            return True
    else:
        return False

def count_func(a,b):
    counter = 0
    for i in range(a,b+1):
        if i%3==0:
                counter += 1
        elif tsn(i):
            counter += 1
    return counter

print(count_func(a,b))
