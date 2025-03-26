word = input()

arr = ["apple","banana","grape","blueberry","orange"]
cnt = 0

for i in range(len(arr)):
    for j in range(2,5):
        if arr[i][j] == word:
            print(arr[i])
            cnt +=1

print(cnt)
        