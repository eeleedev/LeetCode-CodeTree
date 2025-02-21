# 1. N을 입력받음 (체크포인트 개수)
N = int(input())

# 2. N개의 좌표를 리스트에 튜플 형태로 저장
points = [tuple(map(int, input().split())) for _ in range(N)]

# 3. Manhattan 거리 계산 함수
def manhattan(x1,y1,x2,y2):
    manhattan_dist = abs(x1-x2) + abs(y1-y2)
    return manhattan_dist

# 4. 기본 이동 거리 계산 (건너뛰지 않았을 때)
total_distance = sum(
    manhattan(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
    for i in range(N - 1)
)

# 5. 체크포인트 한 개를 건너뛰었을 때의 최소 거리 찾기
min_distance = total_distance

for i in range(1, N - 1):  # 첫 번째와 마지막은 건너뛸 수 없음!
    skip_distance = (
        manhattan(points[i-1][0], points[i-1][1], points[i][0], points[i][1]) +
        manhattan(points[i][0], points[i][1], points[i+1][0], points[i+1][1]) -
        manhattan(points[i-1][0], points[i-1][1], points[i+1][0], points[i+1][1])
    )
    min_distance = min(min_distance, total_distance - skip_distance)

# 6. 결과 출력
print(min_distance)
    
