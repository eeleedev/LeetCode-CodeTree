N = int(input())
answer = 0

def f(n):
    global answer
    # 종료 조건
    if n == 1:
        return answer
    if n % 2 == 0:
        answer += 1
        return f(n//2)
    else:
        answer += 1
        return f(n//3)

print(f(N))