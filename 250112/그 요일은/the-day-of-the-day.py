m1, d1, m2, d2 = map(int, input().split())
A = input()

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_index = days.index(A) # A요일의 인덱스값

def days_calculator(m,d):
    total_days = 0
    for i in range(m-1):
        total_days += month_days[i]
    total_days += d
    return total_days

def day_counter(day_index, difference):
    day_sum = day_index+1
    count = 0 
    if day_sum > difference:
        return count
    else:
        while(True):
            day_sum += 7
            count += 1
            if day_sum > difference: 
                return count 


difference =  days_calculator(m2, d2) - days_calculator(m1, d1) + 1 # 종료 날짜까지 포함
result = day_counter(day_index, difference)
print(result)