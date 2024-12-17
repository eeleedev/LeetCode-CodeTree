n = int(input())

def sequence(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    
    return sequence(a//3)+sequence(a-1)

print(sequence(n))