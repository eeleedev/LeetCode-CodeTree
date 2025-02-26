n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
events = []

# Sweeping algorithm
# Step 1. 이벤트 리스트 만들기(시작점 이벤트(+1), 끝점 이벤트(-1))
for x1,x2 in segments:
    events.append((x1,1)) # 시작점
    events.append((x2,-1)) # 끝점

# Step 2. 정렬
events.sort() # 기본적으로 x좌표 오름차순 정렬

# Step 3: 스위핑하며 최대 겹침 구간 찾기
current_count = 0  # 현재 겹치는 선분 개수
max_count = 0      # 최대 겹침 개수
max_start = -1     # 최대 겹침 구간 시작점
max_end = -1       # 최대 겹침 구간 끝점
active_start = None  # 현재 최대 겹침이 시작된 지점

for x, event in events:
    if event == 1:  # 선분 시작
        current_count += 1
        if current_count > max_count:  # 새로운 최대값 발생
            max_count = current_count
            max_start = x
            active_start = x  # 현재 최대 구간 시작점
    else:  # 선분 종료
        if current_count == max_count:  # 최대 구간이 끝남
            max_end = x
        current_count -= 1

# Step 4: 결과 출력
print(max_count)

