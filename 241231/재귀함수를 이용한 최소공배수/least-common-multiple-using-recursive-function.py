n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(arr):
    if len(arr) == 1:
        return arr[0]
    new_value = (arr[0] * arr[1]) // gcd(arr[0], arr[1])  # 정수 나눗셈으로 수정
    arr = [new_value] + arr[2:]
    return lcm(arr)

print(lcm(arr))  # int() 불필요 (이미 정수)
