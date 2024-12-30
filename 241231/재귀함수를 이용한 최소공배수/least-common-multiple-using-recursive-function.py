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
    new_value = arr[0]*arr[1]//gcd(arr[0],arr[1]) # 최소공배수는 정수로 계산해야 함(정수 나눗셈 사용)
    arr =[new_value] + arr[2:]
    return lcm(arr)

print(lcm(arr))
    