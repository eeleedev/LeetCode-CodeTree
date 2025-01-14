n = int(input())
houses = list(map(int, input().split()))
total_distances = []

for target in range(len(houses)):
    total_distance = 0
    for i in range(len(houses)):
        distance = abs(target - i) # 타겟 집과 다른 집과의 거리
        total_distance += houses[i] * distance
    total_distances.append(total_distance)

minimum = min(total_distances)
print(minimum)
