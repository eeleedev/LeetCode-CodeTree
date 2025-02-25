n = 10
count_list = [0]*6
input_list = list(map(int, input().split()))

for elem in input_list:
    count_list[elem-1]+=1

for i in range(0,6):
    print((i+1),'-',count_list[i])
