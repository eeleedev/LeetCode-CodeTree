a = input()

# 2. 한 자리 숫자인 경우 예외 처리
if len(a) == 1:
    print(0)  # "1" → "0"으로 바꿀 수밖에 없음
    exit()

# 3. 최댓값 변수 초기화
max_value = 0  # 원래 숫자를 비교에서 제외하기 위해 0으로 설정

# 4. 모든 비트를 바꿔보면서 최댓값 찾기
for i in range(len(a)):
    flipped = a[:i] + ('1' if a[i] == '0' else '0') + a[i+1:]
    decimal_value = int(flipped, 2)

    # 5. 반드시 하나를 바꾼 값 중에서 최댓값 갱신
    max_value = max(max_value, decimal_value)

# 6. 최댓값 출력
print(max_value)