class WeatherCast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
cast = [WeatherCast(date,day,weather) for date, day, weather in arr]

rain_caster = []
for i, caster in enumerate(cast):
    if caster.weather == 'Rain':
        rain_caster.append(caster)

rain_caster.sort(key=lambda x: x.date) # date를 기준으로 정렬하기
print(rain_caster[0].date,rain_caster[0].day,rain_caster[0].weather)


# Write your code here!