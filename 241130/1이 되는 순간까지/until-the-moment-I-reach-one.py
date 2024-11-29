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

# def f(n):
#     # 종료 조건
#     if n == 1:
#         return 0
#     if n % 2 == 0:
#         return 1 + f(n // 2)  # 짝수일 때
#     else:
#         return 1 + f(n // 3)  # 홀수일 때

# # 입력 및 출력
# N = int(input())
# print(f(N))