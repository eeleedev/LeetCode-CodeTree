matrix1 = []
matrix2 = []

# 첫 번째 행렬 입력 (빈 줄 무시)
while len(matrix1) < 3:
    row = input().strip()
    if row:  # 빈 줄이 아니면 추가
        matrix1.append(list(map(int, row.split())))

# 두 번째 행렬 입력 (빈 줄 무시)
while len(matrix2) < 3:
    row = input().strip()
    if row:  # 빈 줄이 아니면 추가
        matrix2.append(list(map(int, row.split())))

for i in range(3):
    for j in range(3):
        print(matrix1[i][j]*matrix2[i][j], end=' ')
    print()    