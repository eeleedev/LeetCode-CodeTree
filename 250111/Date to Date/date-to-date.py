m1, d1, m2, d2 = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 1월 1일부터의 일수 세기
def days_calculator(month, day):
    calculate_result = 0
    for i in range(month-1):
        calculate_result += days[i]
    calculate_result += day
    return calculate_result

days1 = days_calculator(m1,d1)
days2 = days_calculator(m2,d2)

print(days2-days1+1)

