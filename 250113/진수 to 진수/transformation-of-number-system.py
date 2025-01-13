a, b = map(int, input().split())
n = list(map(int,input()))

temp = 0
for i in range(len(n)):
    temp = temp * a + n[i]

temp_arr = []

while True:
    if temp < b:
        temp_arr.append(temp)
        break
    temp_arr.append(temp%b)
    temp //= b

temp_arr = temp_arr[::-1]
print(''.join(map(str,temp_arr)))