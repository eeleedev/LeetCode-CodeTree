a, b, c, d = map(int, input().split())

start_time = a * 60 + b
finished_time = c * 60 + d

result = finished_time - start_time
print(result)