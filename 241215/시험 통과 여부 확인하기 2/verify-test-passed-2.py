n = int(input())
scores = [list(map(int,input().split())) for _ in range(n)]
passed_stu = 0

for i in range(n):
    avg = sum(scores[i])/len(scores[i])
    if avg >= 60:
        passed_stu += 1
        print("pass")
    else:
        print("fail")

print(passed_stu)
