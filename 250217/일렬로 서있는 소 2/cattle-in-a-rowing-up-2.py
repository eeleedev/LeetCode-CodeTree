'''
1. N을 입력받는다.
2. N개의 소 키 정보를 리스트 A에 저장한다.
3. 가능한 모든 (i, j, k) 조합을 확인하기 위해 3중 반복문을 사용한다.
   - i는 0부터 N-3까지 반복
   - j는 i+1부터 N-2까지 반복
   - k는 j+1부터 N-1까지 반복
   - 만약 A[i] ≤ A[j] ≤ A[k] 조건을 만족하면 카운트를 증가시킨다.
4. 카운트된 개수를 출력한다.
'''

N = int(input())
A = list(map(int, input().split()))
count = 0


for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if A[i]<=A[j]<=A[k]:
                count += 1

print(count)