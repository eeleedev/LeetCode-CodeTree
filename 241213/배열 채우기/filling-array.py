arr = list(map(int, input().split()))

def find_index():
    if 0 in arr:  # 리스트에 0이 있는지 확인
        return arr.index(0)  # 0의 첫 번째 위치 반환
    return -1  # 0이 없으면 -1 반환

def final_result():
    n = find_index()
    if n != -1:  # 0이 있는 경우
        for i in range(n - 1, -1, -1):  # 0의 앞 요소부터 역순으로 출력
            print(arr[i], end=" ")
    else:  # 0이 없는 경우 전체를 역순으로 출력
        for i in range(len(arr) - 1, -1, -1):  # 전체 리스트에 대해 역순 출력
            print(arr[i], end=" ")

final_result()
