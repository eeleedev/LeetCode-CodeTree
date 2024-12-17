n = int(input())
cnt = 0
arr = [2,4]
def f(a,b,n):
    global cnt
    global result
    if cnt == n :
        return arr[cnt]
    arr.append((arr[a]*arr[b])%100)
    cnt += 1
    return f(a+1,b+1,n)

print(f(0,1,n-1))