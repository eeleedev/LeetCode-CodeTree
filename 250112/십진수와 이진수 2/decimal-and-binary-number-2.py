N = list(map(int,input()))
result_1 = 0

for digit in N:
    result_1 = result_1 * 2 + digit

result_2 = result_1 * 17
final_result = []

while True:
    if result_2 < 2:
        final_result.append(result_2)
        break
    final_result.append(result_2%2)
    result_2 //= 2

final_result = final_result[::-1]
print(''.join(map(str,final_result)))