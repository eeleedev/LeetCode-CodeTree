a = int(input())

for i in range(1,a+1):
    con1 = (i%2==0 and i%4!=0)
    con2 = ((i//8)%2==0)
    con3 = (i%7 < 4)

    if not (con1 or con2 or con3):
        print(i, end=' ')