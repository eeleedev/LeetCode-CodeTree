n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print('*'*i, end=' ')
    print() # 내부 루프가 끝난 후 줄바꿈 추가

# 실행 예시
# n = 4

# 출력:
# **** **** **** **** 
# *** *** *** 
# ** ** 
# * 

