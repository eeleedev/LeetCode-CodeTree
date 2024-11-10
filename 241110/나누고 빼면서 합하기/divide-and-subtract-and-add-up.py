# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# temp = []

# def m_array(n,m):
#     temp.append(m)
#     for _ in range(n):
#         if m%2 == 0:
#             m /= 2
#             temp.append(int(m))
#         else:
#             m -= 1
#             temp.append(int(m))
        
#         if m == 1:
#             break

# m_array(n,m)
# result = 0


# for index in temp:
#     index -= 1
#     result += arr[index]

# print(result)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def sum_sequence(arr, m):
    result = 0
    while m > 1:
        result += arr[m - 1]  # m번째 원소를 더함 (인덱스는 m-1)
        if m % 2 == 0:
            m //= 2  # 짝수일 경우 2로 나눔
        else:
            m -= 1  # 홀수일 경우 1을 뺌
    result += arr[0]  # 마지막으로 m이 1일 때 arr[0]을 더함
    return result

print(sum_sequence(arr, m))