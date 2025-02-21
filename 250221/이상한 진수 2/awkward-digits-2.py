a = input()

# 2. 최댓값 변수 초기화
max_value = int(a, 2)  # 초기값을 현재 숫자의 십진수 값으로 설정

# 3. 두 번째 비트부터 하나씩 바꿔보면서 최댓값 찾기
for i in range(0, len(a)):
    # 현재 비트를 반전 (0 → 1 또는 1 → 0)한 새로운 문자열 생성
    # 문자열은 불변(immutable)이기 때문에 temp[i] 값을 직접 변경할 수 없음
    flipped = a[:i] + ('1' if a[i] == '0' else '0') + a[i+1:]
    # 4. 이진수를 10진수로 변환
    decimal_value = int(flipped, 2)
    # 5. 최댓값 갱신
    max_value = max(max_value, decimal_value)

# 6. 최댓값 출력
print(max_value)