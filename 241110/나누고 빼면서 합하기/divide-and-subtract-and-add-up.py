n, m = map(int, input().split())
arr = list(map(int, input().split()))
temp = []

def m_array(n,m):
    temp.append(m)
    for _ in range(n):
        if m%2 == 0:
            m /= 2
            temp.append(int(m))
        else:
            m -= 1
            temp.append(int(m))
        
        if m == 1:
            break

m_array(n,m)
result = 0


for index in temp:
    index -= 1
    result += arr[index]

print(result)