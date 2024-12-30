n = int(input())
arr = list(map(int,input().split()))

def gcd(a,b):
    if b == 0:
        return a
    if a > b:
        return gcd(b, a%b)
    if b > a:
        return gcd(a, b%a)

def lcm(arr):
    if len(arr) == 1:
        return arr[0]
    new_value = arr[0]*arr[1]/gcd(arr[0],arr[1])
    arr =[new_value] + arr[2:]
    return int(lcm(arr))

print(lcm(arr))
    