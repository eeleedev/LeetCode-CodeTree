a, b, c = map(int, input().split())

criterion_minutes = (10 * 1440) + (11 * 60) + 11

minutes = ((a-1) * 1440) + (b * 60) + c

if minutes-criterion_minutes < 0:
    print('-1')
else:
    print(minutes-criterion_minutes)