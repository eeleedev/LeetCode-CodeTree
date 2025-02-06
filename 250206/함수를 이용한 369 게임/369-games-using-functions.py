a, b = map(int, input().split())

def count_3s6s9s(a, b):
    # 1️⃣ 3의 배수 개수 계산
    count_multiples_of_3 = (b // 3) - ((a - 1) // 3)

    # 2️⃣ 3, 6, 9가 포함된 숫자 개수 (단, 3의 배수는 제외)
    count_contains_3s6s9s = sum(
        1 for i in range(a, b + 1) if i % 3 != 0 and any(c in "369" for c in str(i))
    )

    # 3️⃣ 두 개의 개수를 합쳐 반환
    return count_multiples_of_3 + count_contains_3s6s9s

print(count_3s6s9s(a, b))
