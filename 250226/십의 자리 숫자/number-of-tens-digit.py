input_list = list(map(int, input().split()))
count_list = [0]*9 # 10의 자리 숫자 9개

for i in range(len(input_list)):
    if input_list[i] == 0:
        break
    else:
        temp = input_list[i]//10
        if temp == 0:
            continue
        count_list[temp-1] += 1


for i in range(len(count_list)):
    print(i+1,'-',count_list[i])