long_s = input()
short_s = input()

# 슬라이딩 윈도우 
# 1. long_s의 각 위치에서 short_s와 같은 길이의 문자열을 가져온다.
# 2. 그 문자열이 short_s와 일치하는지 비교한다.
# 3. 일치하면 해당 인덱스를 반환하고, 그렇지 않으면 다음 인덱스로 이동하여 계속 비교한다.
# 4. 만약 문자열 끝까지 비교해도 찾지 못하면 -1을 반환한다.

def find_match_index(long_s, short_s):
    N = len(long_s)
    M = len(short_s)

    for i in range(N - M + 1):
    # (N - M + 1)로 설정하면 i가 N - M까지 도달할 수 있어서, long_s의 마지막 유효한 부분 문자열을 검사할 수 있게 됨.
    # +1을 해주는 이유는 range는 마지막 숫자를 포함하지 않기 때문
        if long_s[i:i+M] == short_s:
        # python에서는 문자열 슬라이싱한 결과를 다른 문자열과 바로 비교가 가능함
            return i
    
    return -1

result = find_match_index(long_s, short_s)
print(result)