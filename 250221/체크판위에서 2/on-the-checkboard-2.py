R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Write your code here!
count = 0  # 점프 가능한 경우의 수 저장

# 모든 시작 위치 (i, j)에서 가능한 점프 탐색
for i in range(R):
    for j in range(C):
        start_color = grid[i][j]  # 현재 위치 색상
        destinations = []  # 점프 가능한 도착 위치 리스트
        
        # 가능한 모든 점프 위치 탐색 (nr > i, nc > j)
        for nr in range(i + 1, R):  # 아래 방향 이동
            for nc in range(j + 1, C):  # 오른쪽 방향 이동
                if grid[nr][nc] != start_color:  # 색이 다르면 점프 가능
                    destinations.append((nr, nc))
        
        # 점프 가능한 위치가 정확히 2개일 때만 count 증가
        if len(destinations) == 2:
            count += 1

print(count)