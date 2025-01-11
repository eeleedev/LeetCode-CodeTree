m1, d1, m2, d2 = map(int, input().split())

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_calculator(m, d):
    days = 0
    for i in range(m-1):
        days += month_days[i]
    days += d
    return days

day_difference = days_calculator(m2,d2) - days_calculator(m1,d1)

exported_index = day_difference % 7

print(days[exported_index])


