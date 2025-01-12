N, B = map(int, input().split())
numbers = []

while True:
    numbers.append(N%B)
    if N < B:
        break
    N //= B
    
numbers = numbers[::-1]
result = "".join(map(str, numbers)) # join 함수는 string일 때만 사용 가능

print(result)