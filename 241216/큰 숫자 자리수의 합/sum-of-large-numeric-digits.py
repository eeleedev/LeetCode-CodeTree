a, b, c = map(int, input().split())
result = a*b*c
sum_answer = 0
def sum_digit(result):
    global sum_answer
    if result == 0 :
        return sum_answer
    num = result % 10
    sum_answer += num
    return sum_digit(result//10)

print(sum_digit(result))